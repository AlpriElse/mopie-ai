from sqlalchemy import String
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

Base = declarative_base()

class VideoMetadata(Base):
  __tablename__ = "user_account"
  
  id: Mapped[str] = mapped_column(primary_key=True)
  title: Mapped[str] = mapped_column(String(100))
  duration: Mapped[int] 
  view_count: Mapped[int]
  upload_date_iso: Mapped[str] = mapped_column(String(10))

  def __repr__(self) -> str:
    return f"VideoMetadata(id={self.id!r}, title={self.title!r}, duration={self.duration!r}), view_count={self.view_count!r}, upload_date_iso={self.upload_date_iso!r})"
