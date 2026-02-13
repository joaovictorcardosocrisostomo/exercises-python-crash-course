def print_models(unprinted, printed):
    """simula a impressão dos objetos"""
    while unprinted:
        current_model = unprinted.pop()
        print(f"Printing {current_model}...")
        printed.append(current_model)

def show_completed(printed):
    """mostra quais objetos foram impressos"""
    print(f"\nEsses modelos foram impressos:")
    for model in printed:
        print(model)