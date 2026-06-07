from fastapi import APIRouter,Depends,HTTPException,status
from sqlmodel import Session,select
from core.database import get_session
from auth.security import hash_password,verify_password,create_access_token
from schemas.user import UserCreate,UserOut,UserLogin,UserUpdate
from models.user import User


router=APIRouter(prefix="auth/",tags=["Authentication"])

@router.post("/register",status_code=status.HTTP_201_CREATED)
def register(user_data:UserCreate,session:Session=Depends(get_session)):

    existing_user=session.exec(select(User).where(User.username==user_data.username)|(User.email==user_data.email)|(User.CIN==user_data.CIN)).first()

    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="اسم المستخدم، البريد الإلكتروني، أو رقم البطاقة الوطنية (CIN) مسجل مسبقاً.")
    
    hashed_pwd=hash_password(user_data.password)

    new_user=User(
        username=user_data.username,
        email=user_data.email,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        CIN=user_data.CIN,
        password=hashed_pwd,
        
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return {"message": "تم إنشاء الحساب بنجاح", "user_id": new_user.id}

@router.patch("/update/{CIN}")
def update_user(CIN:str,user_data:UserUpdate,session:Session=Depends(get_session)):
    user=session.exe(select(User).where(User.CIN==CIN)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="المستخدم غير موجود")
   
    update_data=user_data.model_dump(exclude_unset=True)

    

    for key,value in update_data.items():
        setattr(user,key,value)
    session.add(user)
    session.commit()
    session.refresh(user)
    

@router.post("/login")
def login(user_data:UserLogin,session:Session=Depends(get_session)):
    user=session.exect(select(User).where(User.username==user_data.username)|(User.CIN==user_data.CIN)).first()
    verify_pwd=verify_password(user_data.password,user.password)

    if not user or not verify_pwd:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="اسم المستخدم,رقم البطاقة الوطنية أو كلمة المرور غير صحيحة")
    access_token=create_access_token(data={"sub":str(user.id),"role":user.role})

    return {"access_token":access_token,"token_type":"bearer"}






    
    
    