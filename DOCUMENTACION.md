
Investigar como varia el consumo dependiendo del medio de pago y el lugar de residencia

##4

Tabla Clientes 
id_cliente	int nominal
nombre_cliente str	nominal
email	str nominal
ciudad	str nominal
fecha_alta date intervalo

Tabla Ventas
id_venta int nominal	
fecha	date intervalo
id_cliente	int nominal
nombre_cliente	str nominal
email	str nominal
medio_pago str nominal

Tabla Detalle de Ventas
id_venta int nominal	
id_producto	int nominal
nombre_producto	str nominal
cantidad	int razon
precio_unitario	int razon
importe int razon

Tabla Productos
id_producto	int nominal
nombre_producto	str nominal
categoria	str nominal
precio_unitario int razon