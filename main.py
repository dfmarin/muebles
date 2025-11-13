# ------------------------------------------
# Programa: Mueblería OOP con Herencia y Docstrings
# Autor: ChatGPT
# ------------------------------------------

class Mueble:
    """
    Clase base que representa un mueble genérico en la mueblería.

    Attributes:
        nombre (str): Nombre del mueble.
        tipo (str): Tipo de mueble (por ejemplo: 'Silla', 'Escritorio').
        precio (float): Precio del mueble.
        stock (int): Cantidad disponible en inventario.

    Note:
        It looks like a section, but it will be rendered as an admonition.

    Tip: You can even choose a title.
        This admonition has a custom title!
    """

    def __init__(self, nombre, tipo, precio, stock):
        """
        Inicializa un objeto Mueble.

        Args:
            nombre (str): Nombre del mueble.
            tipo (str): Tipo de mueble.
            precio (float): Precio unitario del mueble.
            stock (int): Cantidad disponible.
        """
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.stock = stock

    def __str__(self):
        """Devuelve una representación legible del mueble."""
        return f"{self.nombre} ({self.tipo}) - ${self.precio} | Stock: {self.stock}"

    def vender(self, cantidad):
        """
        Reduce el stock del mueble si hay suficiente cantidad y calcula el total de la venta.

        Args:
            cantidad (int): Número de unidades a vender.

        Returns:
            float: Total de la venta si se realiza, o 0 si no hay suficiente stock.
        """
        if cantidad <= self.stock:
            self.stock -= cantidad
            total = cantidad * self.precio
            print(f"✅ Venta realizada: {cantidad} x {self.nombre} = ${total}")
            return total
        else:
            print(f"❌ No hay suficiente stock de {self.nombre}.")
            return 0


class Silla(Mueble):
    """
    Clase que representa una silla, hereda de Mueble.

    Atributos adicionales:
        con_respaldo (bool): Indica si la silla tiene respaldo o no.
    """

    def __init__(self, nombre, precio, stock, con_respaldo=True):
        """
        Inicializa una silla con información específica.

        Args:
            nombre (str): Nombre del mueble.
            precio (float): Precio unitario.
            stock (int): Cantidad disponible.
            con_respaldo (bool, opcional): Si la silla tiene respaldo. Por defecto True.
        """
        super().__init__(nombre, "Silla", precio, stock)
        self.con_respaldo = con_respaldo

    def __str__(self):
        """Devuelve una representación legible de la silla."""
        respaldo = "con respaldo" if self.con_respaldo else "sin respaldo"
        return f"{self.nombre} ({self.tipo}, {respaldo}) - ${self.precio} | Stock: {self.stock}"


class Escritorio(Mueble):
    """
    Clase que representa un escritorio, hereda de Mueble.

    Atributos adicionales:
        material (str): Material del escritorio (por ejemplo, 'madera', 'metal').
        con_cajones (bool): Indica si el escritorio tiene cajones.
    """

    def __init__(self, nombre, precio, stock, material="madera", con_cajones=True):
        """
        Inicializa un escritorio con información específica.

        Args:
            nombre (str): Nombre del mueble.
            precio (float): Precio unitario.
            stock (int): Cantidad disponible.
            material (str, opcional): Material del escritorio. Por defecto 'madera'.
            con_cajones (bool, opcional): Si el escritorio tiene cajones. Por defecto True.
        """
        super().__init__(nombre, "Escritorio", precio, stock)
        self.material = material
        self.con_cajones = con_cajones

    def __str__(self):
        """Devuelve una representación legible del escritorio."""
        cajones = "con cajones" if self.con_cajones else "sin cajones"
        return f"{self.nombre} ({self.tipo}, {self.material}, {cajones}) - ${self.precio} | Stock: {self.stock}"


class Cliente:
    """
    Clase que representa un cliente de la mueblería.

    Atributos:
        nombre (str): Nombre del cliente.
        telefono (str): Teléfono de contacto.
    """

    def __init__(self, nombre, telefono):
        """
        Inicializa un cliente.

        Args:
            nombre (str): Nombre del cliente.
            telefono (str): Teléfono del cliente.
        """
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        """Devuelve una representación legible del cliente."""
        return f"Cliente: {self.nombre} | Tel: {self.telefono}"


class Muebleria:
    """
    Clase que representa una mueblería.

    Atributos:
        nombre (str): Nombre de la tienda.
        inventario (list): Lista de objetos tipo Mueble.
        ventas_totales (float): Monto acumulado de las ventas.
    """

    def __init__(self, nombre):
        """
        Inicializa una mueblería con un nombre y un inventario vacío.

        Args:
            nombre (str): Nombre de la mueblería.
        """
        self.nombre = nombre
        self.inventario = []
        self.ventas_totales = 0

    def agregar_mueble(self, mueble):
        """
        Agrega un mueble al inventario.

        Args:
            mueble (Mueble): Objeto que se agregará al inventario.
        """
        self.inventario.append(mueble)
        print(f"🪑 Se agregó {mueble.nombre} al inventario.")

    def mostrar_inventario(self):
        """Muestra todos los muebles disponibles en el inventario."""
        print(f"\n📦 Inventario de {self.nombre}:")
        for mueble in self.inventario:
            print(" -", mueble)

    def vender_mueble(self, nombre_mueble, cantidad, cliente):
        """
        Busca un mueble en el inventario y realiza la venta si hay stock disponible.

        Args:
            nombre_mueble (str): Nombre del mueble a vender.
            cantidad (int): Cantidad de unidades a vender.
            cliente (Cliente): Cliente que realiza la compra.
        """
        for mueble in self.inventario:
            if mueble.nombre.lower() == nombre_mueble.lower():
                total = mueble.vender(cantidad)
                self.ventas_totales += total
                if total > 0:
                    print(f"🧾 Cliente: {cliente.nombre} compró {cantidad} {mueble.nombre}(s).")
                return
        print(f"⚠️ No se encontró el mueble '{nombre_mueble}' en el inventario.")

    def mostrar_ventas_totales(self):
        """Muestra el total de ventas realizadas hasta el momento."""
        print(f"\n💰 Ventas totales: ${self.ventas_totales}")


# ------------------------------------------
# Ejemplo de uso
# ------------------------------------------
if __name__ == "__main__":
    tienda = Muebleria("Muebles El Roble")

    # Crear instancias de muebles
    silla1 = Silla("Silla de oficina", 1500, 8, con_respaldo=True)
    escritorio1 = Escritorio("Escritorio ejecutivo", 5000, 3, material="madera", con_cajones=True)
    escritorio2 = Escritorio("Mesa de estudio", 2800, 5, material="metal", con_cajones=False)

    # Agregar al inventario
    tienda.agregar_mueble(silla1)
    tienda.agregar_mueble(escritorio1)
    tienda.agregar_mueble(escritorio2)

    # Mostrar inventario
    tienda.mostrar_inventario()

    # Crear cliente
    cliente1 = Cliente("Ana López", "555-1234")

    # Venta de una silla
    tienda.vender_mueble("Silla de oficina", 2, cliente1)

    # Mostrar inventario actualizado
    tienda.mostrar_inventario()

    # Total de ventas
    tienda.mostrar_ventas_totales()

