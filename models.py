from sqlalchemy import Column, Integer, String, DateTime
import settings


class Token_common(settings.Base):
    __tablename__ = 'Token_common'

    token_id = Column(Integer, primary_key=True)
    ip_address = Column(String(50), index=True)
    user_identifier = Column(String(50))
    user_id = Column(String(50))
    date_time = Column(DateTime)
    time_zone = Column(String(50))
    method = Column(String(50))
    resource_requested = Column(String(100), index=True)
    protocol = Column(String(50))
    status_code = Column(Integer, index=True)
    size_of_object = Column(Integer)

    def __str__(self):
        return settings.APACHE_COMMON_OUTPUT_FORMAT.format(
            self.token_id, self.ip_address, self.user_identifier,
            self.user_id, str(self.date_time), self.time_zone, self.method,
            self.status_code, self.size_of_object, self.protocol,
            self.resource_requested)


'''
class Token_combined(Base):
    __tablename__ = 'Token_combined'

    token_id = Column(Integer, primary_key=True)
    ip_address = Column(String(50), index=True)
    user_identifier = Column(String(50))
    user_id = Column(String(50))
    date_time = Column(String(50))
    time_zone = Column(String(50))
    method = Column(String(50))
    resource_requested = Column(String(300), index=True)
    protocol = Column(String(50))
    status_code = Column(String(50))
    size_of_object = Column(String(50))
    Referer = Column(String(300))
    User_agent = Column(String(200))


class Token_squid(Base):
    __tablename__ = 'Token_squid'
    pass
'''
