restaurants=['Pistahouse','Mehfil','Bawarchi','Paradise Biryani','kfc']
pistahouse_menu=['Zafrani Biryani:','Mutton Biryani','Fish Biryani','Chicken Biryani+pepsi(250ml)','chicken 65']
Mehfil_menu=['Chicen Biryani','Mutton Biryani','Chicken Dum biryani','chicken 65,','double masala biryani']
Bawarchi_menu=['Hyderabadi biryani','mutton birynai','paneer birynai','veg biryani','starters']
Paradise_menu=['chicken biryani','mutton biryani','Egg noodles','Royal chicken fry piece Biryani','chicken 65']
kfc_menu=['chicken fried rice','chicken zinger','veg zinger','veg rice meal+pepsi','chicken roll']
pistahouse_prices=[239,249,189,169,199]
Mehfil_prices=[149,229,169,199,219]
Bawarchi_prices=[179,199,149,159,99]
Paradise_prices=[249,279,215,299,489]
kfc_prices=[110,150,130,209,129]
cart_item=[]
cart_Q=[]
cart_price=[]
cart_total=[]
import random
while True:
    print('-'*30,'WEL-COME TO FOOD DELIVERY APP','-'*30)
    panel=input('Choose which panel you want(owner/user/exit):')
    if panel=='owner':
        #view all reataurants
        while True:
            print('-'*6,'CHOOSE ANY OPTION','-'*6)
            choose=['1.View Restaurants\n2.Manage Restaurants\n3.Manage Items\n4.View Orders\n5.Report\n6.Logout']
            print(*choose,sep='\n')
            choice=int(input('Choose Option(1-6):'))
            if choice==1:
                print('-'*10,'RESTAURANTS','-'*10)
                print(*restaurants,sep='\n')
            elif choice==2:
                print('-'*10,'MANAGE RESTAURANTS','-'*10)
                view_restaurants=input('Do you want view all restaurants?(yes/no):')
                if view_restaurants=='yes':
                    print(*restaurants,sep='\n')
            #adding new restaurants
                Adding=input('Do you want to add a new restaurant(yes/no):')
                while Adding=='yes':
                    add=input('Enter restaurant name:')
                    if add=='':
                        add=input('Enter valid name:')
                    if add in restaurants:
                         print('restaurant already exist!')
                         add=input('Try to enter new restaurant name')
                    restaurants.append(add)
                    print('New restaurant added sucessfully!!')
                    print(*restaurants,sep='\n')
                    Adding=input('Do you want to add another restaurant(yes/no):')
                    if Adding=='no':
                        break
            #removing restaurants
                remove=input('Do you want to remove a restaurant(yes/no):')
                while remove=='yes':
                    delete=input('Enter a restaurant name for remove:')
                    if delete not in restaurants:
                        print('Restaurant not found')
                        delete=input('Enter valid restaurant name:')
                    if delete in restaurants:
                        restaurants.remove(delete)
                    print('Restaurant removed sucessfully')
                    print(*restaurants,sep='\n')
                    remove=input('Do you want to remove another restaurant(yes/no):')
                    if remove=='no':
                        break
             #modifying restourants
                modify=input('Do you want to modify the restaurants(yes/no):')
                while modify=='yes':
                    modified=input('Enter a restaurant name which restaurant you want to modify:')
                    if modified not in restaurants:
                        print('Restaurant not found')
                        modified=input('Enter valid Restaurant name:')
                    if modified in restaurants:
                        updated=restaurants.index(modified)
                        modifying=input('Enter new restaurant name:')
                        restaurants[updated]=modifying
                    print('Restaurant Modified Sucessfully')
                    print(*restaurants,sep='\n')
                    modify=input('Do you want to modify another restaurants(yes/no):')
                    if modify=='no':
                        break
            elif  choice==3:
                        print('-'*10,'MANAGE ITEMS','-'*10)
                    #adding items
                    #items=input('Do you want add new item in the menu(yes/no):')
                        print('-'*10,'CHOOSE ANY RESTAURANT','-'*10)
                        print(*restaurants,sep='\n')
                        ask=input('Choose restaurant name:')
                        while True:
                            if ask=='kfc': 
                                menu=kfc_menu
                                prices=kfc_prices
                                break
                            elif ask=='Mehfil':
                                menu=Mehfil_menu
                                prices=Mehfil_prices
                                break
                            elif ask=='Pistahouse':
                                menu=pistahouse_menu
                                prices=pistahouse_prices
                                break
                            elif ask=='Bawarchi':
                                menu=Bawarchi_menu
                                prices=Bawarchi_prices
                                break
                            elif ask=='Paradise Biryani':
                                menu=Paradise_menu
                                prices=Paradise_prices
                                break
                            else:
                                print('Restaurant not found')
                            ask=input('Choose correct restaurant name:')
                        for ask in range(len(restaurants)):
                            print(f"{menu[ask]:<30}{prices[ask]}")
                        items=input('Do you want add new item in the menu(yes/no):')
                        while items=='yes':
                            ask=input('Enter item name:')
                            ask1=input('Enter item price:')
                            if ask=='':
                                ask=input('Enter valid item name:')
                            if ask in menu:
                                print('Item already exist:')
                                ask=input('Try to enter new item:')
                                ask1=input('Enter item price:')
                            menu.append(ask)
                            prices.append(ask1)
                            print('New item is added Sucessfully')
                            for ask in range(len(menu)):
                                print(f"{menu[ask]:<30}{prices[ask]}")
                            ask=input('Do you want to add another item(yes/no):')
                            if ask=='no':
                                break
                        items=input('Do you want remove item from the menu(yes/no):')
                        while items=='yes':
                            ask=input('Enter item name:')
                            if ask=='':
                                ask=input('Enter valid item name:')
                            if ask in menu:
                                index=menu.index(ask)
                                menu.remove(ask)
                            prices.pop(index)
                            print('Item is removed Sucessfully')
                            for ask in range(len(menu)):
                                print(f"{menu[ask]:<30}{prices[ask]}")
                            ask=input('Do you want to remove another item(yes/no):')
                            if ask=='no':
                                break
                        items=input('Do you want to modify the restaurants(yes/no):')
                        while items=='yes':
                            modified=input('Enter a restaurant name which restaurant you want to modify:')
                            if modified not in menu:
                                print('Restaurant not found')
                                modified=input('Enter valid Restaurant name:')
                            if modified in menu:
                                updated=menu.index(modified)
                                modifying=input('Enter new restaurant name:')
                                menu[updated]=modifying
                            print('Restaurant Modified Sucessfully')
                            print(*restaurants,sep='\n')
                            modify=input('Do you want to modify another restaurants(yes/no):')
                            if modify=='no':
                                break
            elif choice==4:
                print(' '*2,'item',' '*7,'Quantity',' '*4,'Price',' '*6,'Total',' '*3)
                for item in zip(cart_item, cart_Q, cart_price, cart_total):
                    print(f'{choose_i[0]:<18}{choose_i[1]:<7}{'*'}{' '*7}{choose_i[2]:<13}{choose_i[3]:<5}')
            elif choice==6:
                break       
    elif panel=='user':
        while True:
            print('-'*5,'Please Login','-'*5)
            username=input('Enter username:')
            password=input('Enter password:')
            if username=='hari' and password=='hari@1234':
                print('-'*5,'Login sucessful','-'*5)
                break
            else:
                print('Login failed')
        while True:
            print('1.Browser\n2.Add to cart\n3.Track\n4.Orders\n5.Logout')
            choice=int(input('Choose one option(1-5):'))
            if choice==1:
                print('*'*5,'Restaurants','*'*5,' '*5)
                print(*restaurants,sep='\n')
                ask=input('Enter restaurant name:')
                while True:
                    if ask=='kfc': 
                        menu=kfc_menu
                        prices=kfc_prices
                        break
                    elif ask=='Mehfil':
                        menu=Mehfil_menu
                        prices=Mehfil_prices
                        break
                    elif ask=='Pistahouse':
                        menu=pistahouse_menu
                        prices=pistahouse_prices
                        break
                    elif ask=='Bawarchi':
                        menu=Bawarchi_menu
                        prices=Bawarchi_prices
                        break
                    elif ask=='Paradise Biryani':
                        menu=Paradise_menu
                        prices=Paradise_prices
                        break
                    else:
                        print('Restaurant not found')
                    ask=input('Choose correct restaurant name:')
                for ask in range(len(menu)):
                    print(f"{menu[ask]:<30}{prices[ask]}")
                while True:
                    choose_i=input('select item from menu:')
                    if choose_i in menu:
                        index=menu.index(choose_i)
                        selected_price=prices[index]
                        cart_item.append(choose_i)
                        cart_price.append(selected_price)
                        choose_Q=int(input('Quantity:'))
                        cart_Q.append(choose_Q)    
                        total=selected_price*choose_Q
                        cart_total.append(total)
                        print(cart_item)
                    view=input('view cart(yes/no):')
                    if view=='yes':
                        for item in zip(cart_item, cart_Q, cart_price, cart_total):
                            print(cart_item, cart_Q, cart_price, cart_total)
                    ask=input('Do you want another item(Done):')
                    if ask=='yes':
                        continue
                    if ask=='Done':
                        print(' '*2,'item',' '*7,'Quantity',' '*4,'Price',' '*6,'Total',' '*3)
                        for choose_i in zip(cart_item,cart_Q,cart_price,cart_total):
                            print(f'{choose_i[0]:<18}{choose_i[1]:<7}{'*'}{' '*7}{choose_i[2]:<13}{choose_i[3]:<5}')
                        print('-'*50)
                        t=sum(cart_total)
                        print(' '*35,'Total = ',t)
                        c=input('Apply coupon(text apply):')
                        if c=='apply':
                            s=t*10/100
                            print(' '*24,'you have to pay = ',t-s)
                            print(' '*24,'save',s)
                        else:
                            print('coupon is not applied')
                        order=input('place the order(yes/no)')
                        while order=='yes':
                            payments=['1.phone pay\n2.Google pay\n3.paytm\n4.Navi']
                            print(' '*8,'Payment Options',' '*8)
                            print(*payments,sep='\n')
                            select=int(input('Choose Payment method:'))
                            pay=input('You want to Pay Amount(yes/no):')
                            if pay=='yes':
                                print('---Order Sucessful---')
                                print('Delivery Patner Details')
                                name=['ashok','shiva','sai','prabha']
                                patner=random.choice(name)
                                print('Name',' '*4,'=',' '*5,patner)
                                print('Contact   = ',' '*3,'1234567892')
                            elif pay=='no':
                                continue
                            break
                        break
                #break
            elif choice==2:
                print(' '*2,'item',' '*7,'Quantity',' '*4,'Price',' '*6,'Total',' '*3)
                for choose_i in zip(cart_item,cart_Q,cart_price,cart_total):
                    print(f'{choose_i[0]:<18}{choose_i[1]:<7}{'*'}{' '*7}{choose_i[2]:<13}{choose_i[3]:<5}')
                print('-'*50)
                t=sum(cart_total)
                print(' '*35,'Total = ',t)
            elif choice==3:
                    print('Order Placed')
                    print('|')
                    print('|')
                    print('order on the way')
                    print('|')
                    print('|')
                    print('Order delivered Sucessfully')
            elif choice==4:
                print(' '*2,'item',' '*7,'Quantity',' '*4,'Price',' '*6,'Total',' '*3)
                for item in zip(cart_item, cart_Q, cart_price, cart_total):
                    print(f'{choose_i[0]:<18}{choose_i[1]:<7}{'*'}{' '*7}{choose_i[2]:<13}{choose_i[3]:<5}')
            elif choice==5:
                print('Logout sucessfully')
                break
    elif panel=='exit':
        break
            
            
                
