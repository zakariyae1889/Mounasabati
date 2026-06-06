from sqlmodel import create_engine, Session, SQLModel


# مسار مباشر وصريح وقصير جداً
DATABASE_URL = "sqlite:///mounasabati.db"

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    # سطر واحد مباشر لإنشاء الجداول
    SQLModel.metadata.create_all(engine)

# تشغيل الدالة فوراً عند قراءة الملف
init_db()

def get_session():
    with Session(engine) as session:
        yield session