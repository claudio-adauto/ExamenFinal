# ExamenFinal
virtualenv .venv
source .venv/Scripts/activate
pip install -r requirements.dev.txt

# Preguntas

# 1. Para qué se puede usar Python en lo que respecta a datos. Dar 5 casos y explicar brevemente
Python es muy versátil y ampliamente usado en el análisis de datos, con aplicaciones muy útiles y variadas. Aquí te van cinco casos clave de uso en este campo:

1.- Análisis de Datos: Python permite explorar, limpiar y analizar grandes cantidades de datos. Usando librerías como Pandas y NumPy, se pueden procesar datasets de deportes, redes sociales, o ciencia para obtener información valiosa, detectar patrones y entender tendencias.

2. Visualización de Datos: A través de librerías como Matplotlib, Seaborn y Plotly, se pueden crear gráficos y visualizaciones interactivas que hacen más fácil interpretar los datos. Esto es útil para mostrar patrones de rendimiento en deportes, como el fútbol, o ilustrar las relaciones entre distintas variables.

3. Machine Learning y AI: Con librerías como Scikit-Learn, TensorFlow o PyTorch, Python permite crear modelos de inteligencia artificial que aprenden de los datos. Por ejemplo, puedes entrenar modelos para predecir el rendimiento de jugadores, clasificar imágenes, o analizar texto.

4. Manipulación y Extracción de Datos: Python es ideal para recolectar datos desde APIs o sitios web usando herramientas como BeautifulSoup y Scrapy. Esto permite recolectar datos actualizados, como estadísticas de partidos, puntajes en tiempo real o noticias, para luego analizar y trabajar con ellos.

5. Automatización de Procesos: Python es muy bueno para automatizar tareas repetitivas, como actualizar bases de datos, analizar estadísticas, o generar reportes automáticos de datos. Esto puede ahorrar tiempo y garantizar que la información esté siempre actualizada.
# 2. ¿Cómo se diferencian Flask de Django? Argumentar.
Flask y Django son dos populares frameworks de Python para desarrollar aplicaciones web, pero se diferencian en su enfoque, flexibilidad y arquitectura, entre otros aspectos.

Flask: Es un "micro-framework" que se enfoca en la simplicidad y la flexibilidad. Ofrece solo las funcionalidades básicas, como enrutamiento y gestión de solicitudes, y permite al desarrollador añadir las bibliotecas que prefiera para ampliar la funcionalidad. Esto es ideal para proyectos pequeños o cuando se requiere control total sobre las herramientas utilizadas.

Django: Es un "full-stack framework" que proporciona una solución completa para el desarrollo web. Incluye todo lo necesario, como ORM, autenticación de usuarios, y una interfaz de administración. Esto es útil para aplicaciones 
complejas donde se necesita un flujo de trabajo y estructura definidos.

Flask es ideal para proyectos pequeños o APIs donde la flexibilidad y velocidad son prioritarias, mientras que Django es excelente para aplicaciones complejas que requieren una estructura sólida y herramientas integradas para manejar diferentes aspectos de un sitio web o servicio grande. 
# 3. ¿Qué es un API? Explicar en sus propias palabras
Un API (Interfaz de Programación de Aplicaciones) es un conjunto de reglas y protocolos que permite que diferentes programas se comuniquen entre sí y compartan información o funcionalidades. Esto permite que aplicaciones de diferentes tipos trabajen juntas y se integren.

# 4. ¿Cuál es la principal diferencia entre REST y WebSockets?
La principal diferencia entre REST y WebSockets radica en cómo se comunican entre el cliente y el servidor y en los tipos de aplicaciones para los que están optimizados.

REST: Funciona sobre el protocolo HTTP y sigue un modelo de comunicación basado en solicitudes y respuestas, donde cada interacción es independiente y no hay conexion persistente.

WebSockets: Opera sobre una conexión persistente entre el cliente y el servidor. Una vez que se establece la conexión, ambos pueden enviarse datos en tiempo real, sin necesidad de que el cliente envíe solicitudes repetidas.

REST es ideal para interacciones basadas en solicitudes puntuales y WebSockets para aplicaciones que necesitan comunicación en tiempo real y bidireccional constante.

# 5. Describir un ejemplo de API comercial y como funciona. Usar otros ejemplos no vistos en el curso.
API comercial ampliamente utilizado es la API de pagos de PayPal. Esta API permite a aplicaciones y sitios web integrar pagos de forma segura, permitiendo a los usuarios pagar con sus cuentas de PayPal, tarjetas de crédito, o débito, sin tener que salir de la plataforma.

El funcionamiento es el siguiente:
Se registra la aplicación en la plataforma de PayPal para obtener credenciales de acceso, las cuales permiten a la aplicación acceder a las funcionalidades de la API, como crear, gestionar, y recibir pagos.

Cuando un usuario decide hacer un pago, la aplicación envía una solicitud a la API de PayPal desde el servidor, incluyendo detalles del pago como el monto, la moneda, y una descripción. La API responde con una URL única, que redirige al usuario al sitio de PayPal para iniciar el pago, o muestra una interfaz de pago directamente en la aplicación.

El usuario completa el pago en PayPal, y PayPal notifica a la API que el pago ha sido exitoso. La aplicación recibe un código de confirmación o “token” para verificar que el pago se procesó correctamente.
La aplicación puede consultar el estado de la transacción usando este token para asegurarse de que el pago fue exitoso y que los fondos están en su cuenta de PayPal.

PayPal también ofrece notificaciones en tiempo real que la API envía a la aplicación cada vez que hay una actualización en el estado de una transacción (por ejemplo, si el pago se completó o fue cancelado).
La aplicación puede usar esta información para actualizar la interfaz del usuario o desencadenar otros procesos, como el envío de un producto.

