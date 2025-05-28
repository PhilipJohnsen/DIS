Project for group 40.
Our project is "ZalanDIS", a web-app to browse clothing in all sizes colours and types.

How to compile:
  To compile the program, you must prepare the following files to fit your system.
        1) app/__init__.py
            This file you must change so it fits your PGAdmin server. Change DB Name, user, password, port and host to fit your case.
        2) .venv/pyvenv.cfg
            This file you must change so it fits the location of your Python 3.12.2. This allows for using a virtual machine to run it on. 
        3)  Download images from https://drive.google.com/drive/folders/1hi8ss8tQxoFLmgVTm1-E8g1zi6Xtcuoa?usp=sharing. This is a folder with ~3500 images, 
            the whole folder is just 100mb though. Place these images into app/static/images. The website loads images from this folder only.

  Then we compile it: 
      1) Run init_db.py. This creates tables in your sql server (we used PGADmin 4)
      2) Run import_csv.py. This parses all clothing items into the tables in PGAdmin.
      3) Run run.py. This launches the flask localhost webpage. We use port 5000 as it is typically open.
      4) "Requirements.txt" includes the packages that you must download

  How to interact with the web-app?
      1) Browse clothing by utilising the filters we have implemented to find something to your liking. Colours and sizes and prices and names are synthetically added
         to include these parameters. Therefore you might find a red t-shirt that is labeled as a black t-shirt. The clothing type should fit the image however. 
         That is to say, our filters are working, but our dataset amended random names, colors and sizes so we could make the web-app more realistic.
      2) When you have found an item you wish to purchase, add it to the cart. Add as many items as you want to your cart.
      3) Press "View Cart" to see your items and the total price. If you are satisfied, press "Go to payment"
      4) This displays the checkout which uses RegEx matching. The zip code must be a 4-digit number. The email must be a string followed by one and only one @ symbol, 
         whereafter the domain name is restricted to using letters, dots and dashes. Lastly there must be a ".com" or similar using a dot and at least 2 letters.
         Input your zip code and email address and press "Pay Now" to simulate payment.
      5) The cart gets wiped clean, and you can start your browsing again.
