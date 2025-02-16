coffee = {
    "Coffea arabica" : "The most widely consumed coffee species, known for its smooth, complex flavors and lower caffeine content.",
    "Coffea canephora" : "A hardy species with higher caffeine content, often used in espresso and instant coffee for its strong, bitter taste.",
    "Coffea liberica" : "A species with large, irregular beans and a woody, smoky flavor, mostly grown in West Africa and Southeast Asia.",
    "Coffea excelsa" : "A subspecies of Liberica, offering a tart, fruity profile with light body, commonly used for blending.",
    "Coffea stenophylla" : "Known as 'highland coffee', it has a flavor comparable to Arabica but is more drought-resistant.",
    "Coffea eugenioides" : "A wild species with low caffeine content and mild, sweet flavors; one of Arabica’s parent species.",
    "Coffea racemosa" : "A drought-resistant species from Mozambique with small beans and a mild, tea-like taste.",
    "Coffea congensis" : "A close relative of Robusta, native to the Congo basin, sometimes used in hybrid breeding.",
    "Coffea mauritiana" : "A wild species native to Mauritius, not commercially grown but important for conservation.",
    "Coffea zanguebariae" : "A rare species from East Africa with limited cultivation potential.",
    "Coffea brevipes" : "A wild African coffee species with limited commercial value.",
    "Coffea kianjavatensis" : "A species from Madagascar, sometimes researched for breeding purposes.",
    "Coffea mogeneti" : "A little-known species with restricted growth areas in Africa.",
    "Coffea homollei" : "Native to Madagascar, rarely cultivated.",
    "Coffea resinosa" : "A wild species found in Kenya and Tanzania.",
    "Coffea sessiliflora" : "A small coffee species with slow growth and minor commercial interest.",
    "Coffea togoensis" : "A West African species, mostly found in the wild.",
    "Coffea wightiana" : "A species from India, not cultivated on a large scale.",
    "Coffea myrtifolia" : "A rare species from the Indian Ocean islands.",
    "Coffea ligustroides" : "Native to East Africa, not widely used in cultivation.",
    "Coffea kapakata" : "A species discovered in Angola, showing some potential for cultivation.",
    "Coffea anthonyi" : "A wild hybrid species found in Africa.",
    "Coffea pseudozanguebariae" : "A relative of Zanguebariae with minimal commercial use.",
    "Coffea bacillaris" : "A rare species from Africa, studied for its resistance traits.",
    "Coffea mayombensis" : "Found in the Congo region, with little commercial cultivation.",
    "Coffea perrieri" : "Native to Madagascar, with limited study and cultivation.",
    "Coffea humblotiana" : "A species from the Comoros Islands, facing conservation concerns.",
    "Coffea mannii" : "A rare species from West Africa with minor agricultural interest.",
    "Coffea bonnieri" : "Native to Madagascar, with minimal agricultural use.",
    "Coffea vatovavyensis" : "Another Madagascan species, studied for its genetics rather than for coffee production."
    }

print("Welcome to the Coffee Atlas! We have 30 coffee species in our database.")

while True:
    try:
        print("Definition: ", coffee[input("What species would you like to know?: ")])
    
    except:
        print("Wrong input.")
        
        try:
            print("Definition: ", coffee[input("Would like to search for another?: ")])
    
        except:
            print("Thank you for using Coffee Atlas!")
            break
        