#Dictornaries = collection of {key:value} pairs , NO DUPLICATIONS!
capitals={"USA":"Washington DC",
"India":"New Delhi"
,"Russia":"Moscow",
"China":"Beijing"}

print(capitals.get("USA")) # The value assosiated with the key USA will be printed!
print(capitals.get("Japan")) # There is no key named Japan so the output will be "none"!

capitals.update({"Germany":"Berlin"}) # Basically to add a key-value pair to the dictionary!
# We can update a value for the key too!
# We can use the pop() method to remove a key-value pair!
# popitem() will remove the latest key-value pair updated or inserted!

# The keys() method can be used to get all the keys in a dictionary!
# The values() method can be used to get all the values in a dictionary!
