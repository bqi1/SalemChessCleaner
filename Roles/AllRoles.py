import enum
from Doctor import DoctorRole
from NoRole import BasicRole
# Using enum class create enumerations
class RolesList(enum.Enum):
   doctor = DoctorRole()