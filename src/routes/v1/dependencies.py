from controllers.distribuidores_controller import DistribuidorController
from controllers.empleados_controller import EmpleadoController
from services.distribuidores_service import DistribuidorService
from services.empleados_service import EmpleadoService

# Distribuidor Controllers
distribuidor_service = DistribuidorService(None)
distribuidor_controller = DistribuidorController(distribuidor_service)

# Empleado Controllers
empleado_service = EmpleadoService(None)
empleado_controller = EmpleadoController(empleado_service)
