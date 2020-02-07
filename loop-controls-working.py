#!\usr\bin\env python3

def main():
  print('loop-controls-working.py   main()')
  loop_controls = {'continue':'short the loop back to next iteration','break':'break out of loop','else':'execute only if loop exits normally'}
  
  for k,v in loop_controls.items():
    print(f'{k:10} \t-\t{v:10}')
  
  secret = 'swordfish'
  pw = ''
  auth = False
  count = 0
  max_attempt = 5
  
  while pw!= secret:
    count += 1
    if count > max_attempt: break
    if count==3: continue
    pw = input(f"{count}: What's the secret word?")
    
  else:
    auth=True
  
  print("Authorized" if auth else "Calling the FBI...")
  
  # For loop
  animals =('bear','bunny','dog','cat','velociraptor')
  
  for pet in animals:
    #if pet=='dog':continue
    #if pet=='velociraptor': break
    print(pet)
  else:
    print('that is all of the animals')
  
if __name__ == '__main__': main()