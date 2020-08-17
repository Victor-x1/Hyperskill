spin = input()
charge = input()

if spin == "1/2":
    if charge == "-1/3":
        print(" Strange Quark")
    if charge == "2/3":
        print("Charm Quark")
    if charge == "-1":
        print("Electron Lepton")
    if charge == "0":
        print("Neutrino Lepton")
if spin == "1":
    print("Photon Boson")
