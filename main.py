from models import OrderOfService, CustomMoto, SportsMoto
from estruturas import TabelaHashOficina, MinHeapOficina, PilhaHistoricoOS

# Instanciação das estruturas de dados avançadas da disciplina
estoque_pecas_hash = TabelaHashOficina(tamanho=7)
fila_urgencia_heap = MinHeapOficina()
historico_undo_pilha = PilhaHistoricoOS()
contador_fifo_heap = 0

current_order = None

while True:
  print("\n--- PRISCA REPAIR & CUSTOMIZATION MENU ---")
  print("1. Register New Motorcycle (and set priority)")
  print("2. Add Service to Order")
  print("3. Show Order Summary")
  print("4. Update Budget")
  print("5. Update Status")
  print("6. Manage Parts Catalog (Hash Table)")
  print("7. Process Most Urgent Bike (Min-Heap)")
  print("8. Undo Last Action (Stack / Ctrl+Z)")
  print("9. Exit")

  option = input("Choose an option: ")

  if option == "1":
    print("\nSelect the type of motorcycle:")
    print("1. Custom Moto")
    print("2. Sports Moto")
    bike_type = input("Choose an option: ")

    brand = input("Enter the brand of the motorcycle: ")
    year = int(input("Type the year of the bike: "))
    model = input("Digit the model: ")
    color = input("Enter the color of the motorcycle: ")
    engine_displacement = int(input("Type the engine displacement: "))
        
    # Recolhemos a urgência para alimentar diretamente o Min-Heap
    urgency = int(input("Enter urgency level (1 = Critical/Emergency, 3 = Normal): "))

    if bike_type == "1":
      type_transmission = input("Type transmission (chain/belt): ")
      handlebar_style = input("Handlebar style: ")
      user_moto = CustomMoto(brand, year, model, color, engine_displacement, type_transmission, handlebar_style)
    elif bike_type == "2":
      has_fairing = input("Does it have fairing? (yes/no): ")
      top_speed = int(input("Type the top speed (km/h): "))
      user_moto = SportsMoto(brand, year, model, color, engine_displacement, has_fairing, top_speed)
    else:
      print("Invalid bike type! Defaulting to Custom.")
      user_moto = CustomMoto(brand, year, model, color, engine_displacement, "chain", "standard")

    current_order = OrderOfService(user_moto)
        
    # Inserção automática na Heap de Urgência
    contador_fifo_heap += 1
    fila_urgencia_heap.inserir(urgency, contador_fifo_heap, user_moto)
        
    # Registo da ação na Pilha (para suportar o Ctrl+Z / Desfazer)
    historico_undo_pilha.empilhar(f"Registered bike: {model}")
    print(f"\n{model} successfully registered and added to the Priority Heap!")

  elif option == "2":
    if current_order is None:
      print("Error! You need to register a motorcycle first (Option 1)!")
    
    else:
      service_name = input("What maintenance/customization is desired for the motorcycle?: ")
      current_order.add_service(service_name)
      current_order.save_to_db()
      historico_undo_pilha.empilhar(f"Added service: {service_name}")

  elif option == "3":
    if current_order is None:
      print("Error: No active order found. Register a bike first!")
    else:
      current_order.show_summary()


  elif option == "4":
    if current_order is None:
      print("Error! Register a bike first!")
    else:
      new_value = float(input("Enter the new budget value (R$): "))
      current_order.motorcycle.define_budget(new_value)
      current_order.save_to_db()
      historico_undo_pilha.empilhar(f"Updated budget to {new_value}")

  elif option == "5":
    if current_order is None:
      print("Error! Register a bike first!")
    else:
      print("\nAvailable Statuses: In process, Waiting for parts, Ready to deliver")
      new_status = input("Enter the new status: ")
      current_order.motorcycle.change_status(new_status)
      current_order.save_to_db()
      historico_undo_pilha.empilhar(f"Updated status to {new_status}")

  elif option == "6":
    print("\n--- PARTS CATALOG (HASH TABLE) ---")
    sku = input("Enter Part SKU code (e.g. SKU-101): ")
    part_name = input("Enter part name: ")
    price = float(input("Enter part price: "))
    estoque_pecas_hash.inserir(sku, {"name": part_name, "price": price})
    print(f"Part {sku} saved into Hash Table! Testing instant lookup...")
    found = estoque_pecas_hash.buscar(sku)
    print(f"-> Lookup result for {sku}: {found['name']} (R$ {found['price']}) [O(1) average]")

  elif option == "7":
    print("\n--- PROCESSING MOST URGENT BIKE (MIN-HEAP) ---")
    prox = fila_urgencia_heap.extrair_min()
    if prox:
      urg, ordem, moto = prox
      print(f">> Now servicing: {moto.brand} {moto.model} with Urgency Level {urg}!")
    else:
      print("No bikes in the priority queue.")

  elif option == "8":
    print("\n--- UNDO LAST ACTION (STACK / LIFO) ---")
    last_action = historico_undo_pilha.desempilhar()
    if last_action:
      print(f"[SUCCESS] Reverted action: '{last_action}'")
    else:
      print("No recent actions to undo.")

  elif option == "9":
    print("Closing system. See you space cowboy!")
    break

  else:
        print("Invalid option!")                            

  