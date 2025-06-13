from src.controllers.distribuidores_controller import DistribuidorController
from src.controllers.empleados_controller import EmpleadoController
from src.services.distribuidores_service import DistribuidorService
from src.services.empleados_service import EmpleadoService

# Distribuidor Controllers
distribuidor_service = DistribuidorService()
distribuidor_controller = DistribuidorController(distribuidor_service)

# Empleado Controllers
empleado_service = EmpleadoService()
empleado_controller = EmpleadoController(empleado_service)
