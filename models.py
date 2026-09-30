import sqlite3
#BASE DE DADOS (SQLite)

def init_db():
    conn = sqlite3.connect("repairshop.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT,
            model TEXT,
            year INTEGER,
            color TEXT,
            engine_displacement INTEGER,
            bike_type TEXT,
            services TEXT,
            budget REAL,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

# Inicializa a base de dados
init_db()

# 2. CLASSE MÃE: Motorcycle

class Motorcycle:
  def __init__(self, brand, year, model, color, engine_displacement):
    self.brand = brand
    self.year = year
    self.model = model
    self.color = color
    self.engine_displacement = engine_displacement

    self._service_status = "In process"
    self._estimated_cost = 0.0

  @property
  def service_status(self):
    return self._service_status

  @property
  def estimated_cost(self):
    return self._estimated_cost

  def define_budget(self, value):
    self._estimated_cost = value
    print(f"The budget for {self.model} updated to: R$ {self._estimated_cost}.")

  def change_status(self, new_status):
    self._service_status = new_status
    print(f"Status of {self.model} updated to: '{self._service_status}'.")

# 3. SUBCLASSES: CUSTOM E SPORTS (Herança)

class CustomMoto(Motorcycle):
  def __init__(self, brand, year, model, color, engine_displacement, type_transmission, handlebar_style):
    super().__init__(brand, year, model, color, engine_displacement)
    self.type_transmission = type_transmission
    self.handlebar_style = handlebar_style


class SportsMoto(Motorcycle):
  def __init__(self, brand, year, model, color, engine_displacement, has_fairing, top_speed):
    super().__init__(brand, year, model, color, engine_displacement)
    self.has_fairing = has_fairing
    self.top_speed = top_speed


# 4. ORDEM DE SERVIÇO (OrderOfService)
class OrderOfService:
  def __init__(self, motorcycle):
    self.motorcycle = motorcycle
    self.services = []
    self.id = None

  def add_service(self, service_description):
    self.services.append(service_description)
    print(f"The service '{service_description}' added to the {self.motorcycle.model}.")

  def save_to_db(self):
    conn = sqlite3.connect("repairshop.db")
    cursor = conn.cursor()

    bike_type = "Custom" if isinstance(self.motorcycle, CustomMoto) else "Sports"
    services_str = ", ".join(self.services)

    if self.id is None:
      # Inserir nova ordem se ainda não tiver ID
      cursor.execute(
        """
        INSERT INTO orders (brand, model, year, color, engine_displacement, bike_type, services, budget, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
          self.motorcycle.brand, self.motorcycle.model, self.motorcycle.year,
          self.motorcycle.color, self.motorcycle.engine_displacement,
          bike_type, services_str, self.motorcycle.estimated_cost,
          self.motorcycle.service_status,
        ),
      )
      self.id = cursor.lastrowid
      print(f"New order of service was generated in our bank! ID: {self.id}")

  def show_summary(self):
    print("\n========================================")
    print(f"        SUMMARY - ORDER OF SERVICE        ")
    print("========================================")
    print(f"Motorcycle: {self.motorcycle.brand} {self.motorcycle.model} ({self.motorcycle.color})")
    print(f"Status: {self.motorcycle._service_status}")
    print(f"Total Budget: R$ {self.motorcycle._estimated_cost}")
    print("----------------------------------------")
    print("Services Performed:")
    for service in self.services:
      print(f" - {service}")
    print("========================================\n")  







      