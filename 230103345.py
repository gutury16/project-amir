import tkinter as tk
import tkinter.messagebox
import pickle as pe
import os

class Toyota:
    def __init__(self, model, turbins, volume, r_busbar, color, fuel, transmission, air_conditional, price, heated_seats):
        self.model = model
        self.turbins = turbins
        self.volume = volume
        self.r_busbar = r_busbar
        self.color = color
        self.fuel = fuel
        self.transmission = transmission
        self.air_conditional = air_conditional
        self.price = price
        self.heated_seats = heated_seats
class Camry(Toyota):
    def __init__(self, model, turbins, volume, r_busbar, color, fuel, transmission, air_conditional, price, heated_seats):
        super().__init__(str(model), turbins, volume, r_busbar, color, fuel, transmission, air_conditional, price, heated_seats)

class LandCruiser(Toyota):
    def __init__(self, model, turbins, volume, r_busbar, color, fuel, transmission, air_conditional, price, heated_seats):
        super().__init__(str(model), turbins, volume, r_busbar, color, fuel, transmission, air_conditional, price, heated_seats)
cars_list = [
    Camry(75, 4, 4.8, "R16", "black", "gas and petrol", "automatic", "Yes", 16500000, "Yes"),
    Camry(70, 3, 4.5, "R16", "white", "gas and petrol", "automatic", "Yes", 14300000, "Yes"),
    Camry(55, 2, 2.2, "R15", "white", "gas and petrol", "automatic", "Yes", 12000000, "Yes"),
    Camry(50, 2, 2.0, "R15", "silver", "gas and petrol", "manual", "Yes", 10450000, "Yes"),
    Camry(45, 2, 1.8, "R14", "gold", "petrol", "manual", "Yes", 7000000, "No"),
    Camry(40, 2, 1.8, "R14", "black", "petrol", "manual", "Yes", 5650000, "No"),
    Camry(35, 2, 1.6, "R14", "black", "petrol", "mechanic", "Yes", 4600000, "No"),
    Camry(30, 1, 1.6, "R14", "gold", "petrol", "mechanic", "No", 4200000, "No"),
    Camry(25, 1, 1.4, "R13", "silver", "petrol", "mechanic", "No", 3700000, "No"),
    Camry(20, 1, 1.4, "R13", "burgundy", "petrol", "mechanic", "No", 3000000, "No"),
    Camry(15, 1, 1.2, "R12", "silver", "petrol", "mechanic", "No", 2000000, "Yes"),
    Camry(10, 1, 1.2, "R12", "white", "petrol", "mechanic", "No", 1600000, "No"),

    LandCruiser(300, 6, 5.6, "R17", "white", "gas and petrol","automatic", "Yes", 55000000, "Yes"),
    LandCruiser(250, 6, 5.4, "R17", "silver", "gas and petrol", "automatic", "Yes", 45000000, "Yes"),
    LandCruiser(200, 6, 5.2, "R17", "white", "gas and petrol", "automatic", "Yes", 30000000, "Yes"),
    LandCruiser(150, 6, 5.0, "R17", "black", "gas and petrol", "automatic", "Yes", 20500000, "Yes"),
    LandCruiser(100, 6, 4.8, "R17", "silver", "petrol", "automatic", "Yes", 18800000, "Yes"),
]
hidden_cars_list = []
def display_main_menu_image():
    main_menu_image_path = r"C:\Users\Amir\Desktop\project amir\bg1.png" 
    display_image_tk(main_menu_image_path, side="bottom")

def display_image_tk(image_path, side="bottom"):
    try:
        image = tk.PhotoImage(file=image_path)
        image_label = tk.Label(win, image=image)
        image_label.image = image
        image_label.pack(side=side, fill="both", expand="yes")
    except tk.TclError:
        print(f"Image file not found: {image_path}")

with open('camry_list.pe', 'wb') as file:
    pe.dump(cars_list, file)

hidden_cars_list_filename = 'hidden_cars_list.pe'

def save_hidden_cars_list():
    with open(hidden_cars_list_filename, 'wb') as file:
        pe.dump(hidden_cars_list, file)

def load_hidden_cars_list():
    try:
        with open(hidden_cars_list_filename, 'rb') as file:
            return pe.load(file)
    except FileNotFoundError:
        return []

hidden_cars_list = load_hidden_cars_list()

def display_car_info(car):
    info = (
        f"Car model: {car.model}\n"
        f"Number of turbins: {car.turbins}\n"
        f"Engine capacity: {car.volume}\n"
        f"Radius of busbar: {car.r_busbar}\n"
        f"Car color: {car.color}\n"
        f"Fuel type: {car.fuel}\n"
        f"Transmission: {car.transmission}\n"
        f"Is there an air conditioner in the car? {car.air_conditional}\n"
        f"Does the car have heated seats? {car.heated_seats}\n"
        f"Car price: {car.price}"
    )
    return info

def add_car(model, turbins, volume, r_busbar, color, fuel, transmission, air_conditional, price, heated_seats, car_type):
    try:
        model = int(model)

     
        existing_car_visible = next((car for car in cars_list if car.model == model and isinstance(car, Camry)), None)
        existing_car_hidden = next((car for car in hidden_cars_list if car.model == model and isinstance(car, Camry)), None)

        if existing_car_visible or existing_car_hidden:
            tk.messagebox.showerror("Error", f"Camry with model {model} already exists")
            return

        if car_type == 'Camry':
       
            if not (1 <= model <= 99):
                tk.messagebox.showerror("Error", "Camry model must be between 1 and 99")
                return
        elif car_type == 'LandCruiser':
        
            pass
        else:
            tk.messagebox.showerror("Error", "Invalid car type")
            return
    except ValueError:
        tk.messagebox.showerror("Error", "Model must be a number")
        return

    if car_type == 'Camry':
        new_car = Camry(model, turbins, volume, r_busbar, color, fuel, transmission, air_conditional, price, heated_seats)
        success_message = f"Camry {model} added successfully"
    elif car_type == 'LandCruiser':
        new_car = LandCruiser(model, turbins, volume, r_busbar, color, fuel, transmission, air_conditional, price, heated_seats)
        success_message = f"LandCruiser {model} added successfully"
    else:
        tk.messagebox.showerror("Error", "Invalid car type")
        return

    cars_list.append(new_car)
    tk.messagebox.showinfo("Success", success_message)




def delete_car(car_type, model):
    global hidden_cars_list

    if car_type not in ['Camry', 'LandCruiser']:
        tk.messagebox.showerror("Error", "Invalid car type")
        return

    car_class = Camry if car_type == 'Camry' else LandCruiser

    print(f"Deleting car - Type: {car_type}, Model: {model}")

    car_to_delete = next((car for car in cars_list if str(car.model) == str(model) and isinstance(car, car_class)), None)

    print(f"cars_list: {cars_list}")
    print(f"model to delete: {model}")

    if car_to_delete:
        cars_list.remove(car_to_delete)
        hidden_cars_list.append(car_to_delete)
        tk.messagebox.showinfo("Success", f"Car {car_type} - {model} deleted and moved to hidden cars")
        save_hidden_cars_list()
    else:
        tk.messagebox.showerror("Error", f"{car_type} - {model} not found in visible cars")

def remove_hidden_cars():
    global hidden_cars_list, cars_list
    cars_list = [car for car in cars_list if car not in hidden_cars_list]
    hidden_cars_list = []
    tk.messagebox.showinfo("Success", "Hidden cars removed successfully")
    save_hidden_cars_list()

def save_hidden_cars_list():
    with open(hidden_cars_list_filename, 'wb') as file:
        pe.dump(hidden_cars_list, file)



def show_hidden_cars():
    clear_window()
    for car in hidden_cars_list:
        model_button = tk.Button(win, text=f"Hidden - {car.model}", command=lambda model=car.model: on_hidden_button_click(model), height=3, width=20)
        model_button.pack()
    
    button_remove_hidden = tk.Button(win, text="Remove Hidden Cars", command=remove_hidden_cars, height=3, width=25)
    button_remove_hidden.pack()

    button_back = tk.Button(win, text="Back", command=after_login_menu)
    button_back.pack()

def on_button_click(car_model):
    selected_model = next((car for car in cars_list if car.model == car_model), None)

    if selected_model:
        if isinstance(selected_model, Camry):
            info = display_car_info(selected_model)
            show_car_info_with_image(info, selected_model)
        elif isinstance(selected_model, LandCruiser):
            info = display_car_info(selected_model)
            show_car_info_with_image(info, selected_model)
        else:
            tk.messagebox.showerror("Error", "Invalid car type")
    else:
        selected_hidden_model = next((car for car in hidden_cars_list if str(car.model) == str(car_model)), None)
        if selected_hidden_model:
            if isinstance(selected_hidden_model, Camry):
                info = display_car_info(selected_hidden_model)
                show_car_info_with_image(info, selected_hidden_model, True)
            elif isinstance(selected_hidden_model, LandCruiser):
                info = display_car_info(selected_hidden_model)
                show_car_info_with_image(info, selected_hidden_model, True)
            else:
                tk.messagebox.showerror("Error", "Invalid hidden car type")
        else:
            tk.messagebox.showerror("Error", "Incorrect model number")



def show_car_info_with_image(info, selected_model):
    popup = tk.Toplevel()
    popup.title("Information about the car")

    info_label = tk.Label(popup, text=info, padx=10, pady=10, justify=tk.LEFT)
    info_label.pack()

    image_folder_path = r"C:\Users\Amir\Desktop\project amir"
    image_path = f"{image_folder_path}\\ready{selected_model.model}_{selected_model.__class__.__name__.lower()}.png"

    try:
        image = tk.PhotoImage(file=image_path)
        image_label = tk.Label(popup, image=image)
        image_label.image = image  
        image_label.pack()
    except tk.TclError:
        print(f"Image file not found: {image_path}")

win = tk.Tk()
win.title('Amir Company')

win.geometry("1200x1200")


def clear_window():
    for widget in win.winfo_children():
        widget.destroy()

def main_menu():
    clear_window()
    display_main_menu_image()
    login_button = tk.Button(win, text="Login", command=login, height=3, width=20)
    registration_button = tk.Button(win, text="Sign up", command=registration, height=3, width=20)
    login_button.pack()
    registration_button.pack()

def back_to_main():
    main_menu()

def show_land_cruiser_models():
    clear_window()
    display_main_menu_image()
    for car in cars_list:
        if isinstance(car, LandCruiser):
            model_button = tk.Button(win, text=car.model, command=lambda model=car.model: on_button_click(model), height=3, width=20)
            model_button.pack()
    button_back = tk.Button(win, text="Back", command=after_login_menu)
    button_back.pack()

def tune_car_menu():
    clear_window()

    selected_model_var = tk.StringVar()
    turbins_var = tk.StringVar()
    fuel_var = tk.StringVar()
    transmission_var = tk.StringVar()

    model_options = [f"{car.model} - {car.__class__.__name__}" for car in cars_list if car not in hidden_cars_list]
    if not model_options:
        tk.messagebox.showinfo("Information", "There are no tuning machines available.")
        after_login_menu()
        return

    selected_model_var.set(model_options[0]) 

    label_select_model = tk.Label(win, text="Choose model for tuning:")
    dropdown_model = tk.OptionMenu(win, selected_model_var, *model_options)
    label_turbins = tk.Label(win, text="New counf of turbins:")
    entry_turbins = tk.Entry(win, textvariable=turbins_var)
    label_fuel = tk.Label(win, text="New type of fuel:")
    entry_fuel = tk.Entry(win, textvariable=fuel_var)
    label_transmission = tk.Label(win, text="New type of transmission:")
    entry_transmission = tk.Entry(win, textvariable=transmission_var)

    button_tune = tk.Button(win, text="Tuning", command=lambda: tune_car(
        selected_model_var.get(), turbins_var.get(), fuel_var.get(), transmission_var.get()
    ))
    button_back = tk.Button(win, text="Back", command=after_login_menu)

    label_select_model.pack()
    dropdown_model.pack()
    label_turbins.pack()
    entry_turbins.pack()
    label_fuel.pack()
    entry_fuel.pack()
    label_transmission.pack()
    entry_transmission.pack()
    button_tune.pack()
    button_back.pack()

def about_toyota():
    clear_window()
    text = (
        "Toyota Motor Corporation is a Japanese multinational automotive manufacturer founded in 1937 by Kiichiro Toyoda.\n\n"
        "Toyota is one of the largest and most well-known car manufacturers globally, with a rich history of innovation and excellence.\n\n"
        "Key Points:\n"
        "- Founder: Kiichiro Toyoda\n"
        "- Headquarters: Toyota City, Aichi, Japan\n"
        "- Global Presence: Toyota operates in more than 170 countries worldwide.\n"
        "- Industry Leadership: Toyota has consistently been at the forefront of automotive technology and production.\n"
        "- Sustainable Practices: Toyota is committed to environmental sustainability and has been a pioneer in hybrid and electric vehicles.\n\n"
        "Toyota offers a diverse range of vehicles, catering to various market segments:\n"
        "- Compact Cars: Economical and fuel-efficient models suitable for urban commuting.\n"
        "- Sedans: Including the popular Camry series known for its comfort and reliability.\n"
        "- SUVs and Crossovers: Combining versatility with advanced safety features.\n"
        "- Trucks and Vans: Rugged and durable vehicles for commercial and personal use.\n\n"
        "In addition to its commitment to producing high-quality vehicles, Toyota is actively involved in philanthropy, community engagement, and technological advancements for the future of mobility.")
    label_about_toyota = tk.Label(win, text=text, padx=10, pady=10, justify=tk.LEFT)
    label_about_toyota.pack()
    
    button_back = tk.Button(win, text="Back", command=after_login_menu)
    button_back.pack()

def about_camry():
    clear_window()
    text = (
        "The 'Camry' is a distinguished series of mid-size and full-size cars crafted by the eminent Japanese automaker, 'Toyota.' "
        "Introduced in 1982, the 'Camry' swiftly ascended to become one of the globally best-selling cars.\n\n"
        "Recognized for its steadfast reliability, commendable fuel efficiency, and a ride that exudes comfort, the 'Camry' has consistently "
        "secured its position as a preferred choice for both families and individuals.\n\n"
        "The 'Camry' lineup is characterized by its diverse models, each presenting a range of engine options, features, and designs. "
        "This variety allows consumers to select a model that aligns precisely with their preferences, whether in terms of performance, "
        "amenities, or aesthetics.\n\n"
        "In addition to its renowned performance on the road, the 'Camry' places a strong emphasis on technological innovation and modern "
        "conveniences within the vehicle. The interior is designed to provide an optimal driving experience, integrating intuitive infotainment "
        "systems, advanced safety features, and thoughtful ergonomic details.\n\n"
        "As the automotive landscape advances, the 'Camry' remains a testament to 'Toyota's' dedication to innovation, reliability, and customer "
        "satisfaction. It continues to stand out as a stalwart choice for those seeking a harmonious blend of performance, comfort, and style "
        "in their driving experience."
    )

    label_about_camry = tk.Label(win, text=text, padx=10, pady=10, justify=tk.LEFT, wraplength=400)  
    label_about_camry.pack()

    button_back = tk.Button(win, text="Back", command=after_login_menu)
    button_back.pack()


def about_land_cruiser():
    clear_window()
    text = (
        "Land Cruiser is a series of four-wheel-drive vehicles produced by Toyota. It is one of the oldest and most iconic SUVs in the automotive industry.\n\n"
        "The Land Cruiser is known for its off-road capabilities, durability, and versatility. It has been used for various purposes, from family adventures to expedition and exploration.\n\n"
        "The Land Cruiser comes in different models, offering a combination of luxury and ruggedness."
    )
    label_about_land_cruiser = tk.Label(win, text=text, padx=10, pady=10, justify=tk.LEFT)
    label_about_land_cruiser.pack()
    
    button_back = tk.Button(win, text="Back", command=after_login_menu)
    button_back.pack()


def tune_car(selected_model_str, new_turbins, new_fuel, new_transmission):
    display_main_menu_image()
    try:
        selected_model_parts = selected_model_str.split(" - ")
        model = int(selected_model_parts[0])
        car_class_name = selected_model_parts[1]
        car_class = Camry if car_class_name == "Camry" else LandCruiser

        selected_car = next((car for car in cars_list if car.model == str(model) and isinstance(car, car_class)), None)

        if selected_car:
            if new_turbins:
                selected_car.turbins = int(new_turbins)
            if new_fuel:
                selected_car.fuel = new_fuel
            if new_transmission:
                selected_car.transmission = new_transmission

            tk.messagebox.showinfo("Success", f"Car {model} successfully tuned")
        else:
            tk.messagebox.showerror("Error", f"Car {model} not found in the list")

    except ValueError:
        tk.messagebox.showerror("Error", "Data entry error. Make sure that the correct values are entered.")



def after_login_menu():
    clear_window()
    display_main_menu_image()
    
    choose_camry_button = tk.Button(win, text="Choose Camry model", command=show_camry_models, height=3, width=20)
    choose_camry_button.pack()
    
    choose_land_cruiser_button = tk.Button(win, text="Choose Land Cruiser model", command=show_land_cruiser_models, height=3, width=25)
    choose_land_cruiser_button.pack()
    
    tune_button = tk.Button(win, text="Tuning", command=tune_car_menu, height=3, width=20)
    tune_button.pack()
    
    add_car_button = tk.Button(win, text="Add Car", command=add_car_menu, height=3, width=20)
    add_car_button.pack()
    
    delete_car_button = tk.Button(win, text="Delete Car", command=delete_car_menu_gui_func, height=3, width=20)
    delete_car_button.pack()
    
    show_hidden_button = tk.Button(win, text="Hidden Cars", command=show_hidden_cars, height=3, width=20)
    show_hidden_button.pack()

    button_about_toyota = tk.Button(win, text="About Toyota", command=about_toyota, height=3, width=20)
    button_about_camry = tk.Button(win, text="About Camry", command=about_camry, height=3, width=20)
    button_about_land_cruiser = tk.Button(win, text="About LandCruiser", command=about_land_cruiser, height=3, width=25)
    button_about_toyota.pack()
    button_about_camry.pack()
    button_about_land_cruiser.pack()
    
    button_back = tk.Button(win, text="Back", command=back_to_main)
    button_back.pack()
    

def add_car_menu():
    clear_window()
    display_main_menu_image()
    text_model = tk.Label(win, text="Enter model:")
    enter_model = tk.Entry(win)
    text_turbins = tk.Label(win, text="Enter number of turbins:")
    enter_turbins = tk.Entry(win)
    text_volume = tk.Label(win, text="Enter engine capacity:")
    enter_volume = tk.Entry(win)  
    text_r_busbar = tk.Label(win, text="Enter radius of busbar:")
    enter_r_busbar = tk.Entry(win)  
    text_color = tk.Label(win, text="Enter color:")
    enter_color = tk.Entry(win)  
    text_fuel = tk.Label(win, text="Enter fuel type:")
    enter_fuel = tk.Entry(win)  
    text_transmission = tk.Label(win, text="Enter transmission type:")
    enter_transmission = tk.Entry(win)  
    text_air_conditional = tk.Label(win, text="Enter air conditioner presence (Yes/No):")
    enter_air_conditional = tk.Entry(win)
    text_price = tk.Label(win, text="Enter car price:")
    enter_price = tk.Entry(win) 
    text_heated_seats = tk.Label(win, text="Enter heated seats presence (Yes/No):")
    enter_heated_seats = tk.Entry(win)
    text_type = tk.Label(win, text="Enter car type (Camry/LandCruiser):")
    enter_type = tk.Entry(win)
    button_add = tk.Button(win, text="Add Car", command=lambda: add_car(
        enter_model.get(), enter_turbins.get(), enter_volume.get(),
        enter_r_busbar.get(), enter_color.get(), enter_fuel.get(),
        enter_transmission.get(), enter_air_conditional.get(),
        enter_price.get(), enter_heated_seats.get(), enter_type.get()
    ), height=3, width=20)
    button_back = tk.Button(win, text="Back", command=after_login_menu)
    
    text_model.pack()
    enter_model.pack()
    text_turbins.pack()
    enter_turbins.pack()
    text_volume.pack()
    enter_volume.pack()
    text_r_busbar.pack()
    enter_r_busbar.pack()
    text_color.pack()
    enter_color.pack()
    text_fuel.pack()
    enter_fuel.pack()
    text_transmission.pack()
    enter_transmission.pack()
    text_air_conditional.pack()
    enter_air_conditional.pack()
    text_price.pack()
    enter_price.pack()
    text_heated_seats.pack()
    enter_heated_seats.pack()
    text_type.pack()
    enter_type.pack()
    button_add.pack()
    button_back.pack()



def delete_car_menu_gui_func():
    clear_window()
    display_main_menu_image()
    text_type = tk.Label(win, text="Enter car type (Camry/LandCruiser):")
    enter_type = tk.Entry(win)
    text_model = tk.Label(win, text="Enter model to delete:")
    enter_model = tk.Entry(win)
    button_delete = tk.Button(win, text="Delete Car", command=lambda: delete_car_func(enter_type.get(), enter_model.get()), height=3, width=20)
    button_back = tk.Button(win, text="Back", command=after_login_menu)
    
    text_type.pack()
    enter_type.pack()
    text_model.pack()
    enter_model.pack()
    button_delete.pack()
    button_back.pack()

def delete_car_func(car_type, model):
    global hidden_cars_list, cars_list

    if car_type not in ['Camry', 'LandCruiser']:
        tk.messagebox.showerror("Error", "Invalid car type")
        return

    car_class = Camry if car_type == 'Camry' else LandCruiser
    
    try:
        model = int(model)
    except ValueError:
        tk.messagebox.showerror("Error", "Model must be a number")
        return

    car_to_delete = next((car for car in cars_list if str(car.model) == str(model) and isinstance(car, car_class)), None)

    if car_to_delete:
        cars_list.remove(car_to_delete)
        hidden_cars_list.append(car_to_delete)
        tk.messagebox.showinfo("Success", f"Car {car_type} - {model} deleted and moved to hidden cars")
        save_hidden_cars_list()
    else:
        tk.messagebox.showerror("Error", f"{car_type} - {model} not found in visible cars")


def login():
    def log_pass():
        try:
            with open("login.txt", "rb") as a:
                while True:
                    try:
                        b = pe.load(a)
                        if enter_login.get() in b:
                            if enter_password.get() == b[enter_login.get()]:
                                tk.messagebox.showinfo("Success", "Login completed successfully")
                                after_login_menu()
                                return
                            else:
                                tk.messagebox.showerror("Error", "Error, invalid password or login")
                                return
                    except EOFError:
                        break
            tk.messagebox.showerror("Error, invalid login")
        except FileNotFoundError:
            tk.messagebox.showerror("Error!", "Database file not found")

    clear_window()
    display_main_menu_image()
    text_log = tk.Label(win, text="Congratulations, you are now a user of our system!")
    text_enter_login = tk.Label(win, text="Enter your username: ")
    enter_login = tk.Entry(win)
    text_enter_password = tk.Label(win, text="Enter your password: ")
    enter_password = tk.Entry(win, show="*")
    button_enter = tk.Button(win, text="Enter", command=log_pass)
    button_back = tk.Button(win, text="Back", command=back_to_main)
    text_log.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_password.pack()
    enter_password.pack()
    button_enter.pack()
    button_back.pack()

def registration():
    def save():
        if registr_password1.get() == registr_password2.get():
            login_pass_save = {registr_login.get(): registr_password1.get()}
            with open("login.txt", "ab") as a:
                pe.dump(login_pass_save, a)
            tk.messagebox.showinfo("Success", "Registration is successful")
            main_menu()
        else:
            tk.messagebox.showerror("Error","Error, invalid password or login")

    clear_window()
    display_main_menu_image()
    text = tk.Label(win, text="To log in, you need to register")
    text_log = tk.Label(win, text="Enter your username: ")
    registr_login = tk.Entry(win)
    text_password1 = tk.Label(win, text="Enter your password: ")
    registr_password1 = tk.Entry(win, show="*")
    text_password2 = tk.Label(win, text="Enter your password again:")
    registr_password2 = tk.Entry(win, show="*")
    button_registr = tk.Button(win, text="Sign up", command=save)
    button_back = tk.Button(win, text="Back", command=back_to_main)
    text.pack()
    text_log.pack()
    registr_login.pack()
    text_password1.pack()
    registr_password1.pack()
    text_password2.pack()
    registr_password2.pack()
    button_registr.pack()
    button_back.pack()

def on_hidden_button_click(car_model):
    selected_model = next((car for car in hidden_cars_list if car.model == car_model), None)
    if selected_model:
        info = display_car_info(selected_model)
        show_car_info_with_image(info, selected_model)
    else:
        tk.messagebox.showerror("Error", "Incorrect model number")


def show_car_info_with_image(info, selected_model, is_hidden=False):
    global popup
    popup = tk.Toplevel()
    popup.title("Information about the car")

    info_label = tk.Label(popup, text=info, padx=10, pady=10, justify=tk.LEFT)
    info_label.pack()

    image_folder_path = r"C:\Users\Amir\Desktop\project amir"
    image_path = f"{image_folder_path}\\{selected_model.__class__.__name__.lower()}{selected_model.model}.png"

    try:
        image = tk.PhotoImage(file=image_path)
        image_label = tk.Label(popup, image=image)
        image_label.image = image  
        image_label.pack()
    except tk.TclError:
            print(f"Image file not found: {image_path}")

    if is_hidden:
        button_delete = tk.Button(
            popup,
            text="Delete",
            command=lambda model=selected_model.model: delete_hidden_car(model),
            height=2,
            width=15
        )
        button_delete.pack()

    win.wait_window(popup)

def delete_hidden_car(model):
    car_class = Camry
    car_to_delete = next((car for car in hidden_cars_list if car.model == model and isinstance(car, car_class)), None)

    if car_to_delete:
        hidden_cars_list.remove(car_to_delete)
        cars_list.append(car_to_delete)
        tk.messagebox.showinfo("Success", f"Car {model} deleted from hidden cars")
        save_hidden_cars_list()
        popup.withdraw()  
    else:
        tk.messagebox.showerror("Error", "Car not found")




def show_camry_models():
    clear_window()
    for car in cars_list:
        if isinstance(car, Camry) and car not in hidden_cars_list:
            model_button = tk.Button(win, text=f"Camry - {car.model}", command=lambda model=car.model: on_button_click(model), height=3, width=20)
            model_button.pack()
    button_back = tk.Button(win, text="Back", command=after_login_menu)
    button_back.pack()





main_menu()  
win.mainloop()