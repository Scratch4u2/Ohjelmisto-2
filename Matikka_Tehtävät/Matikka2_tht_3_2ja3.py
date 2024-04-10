import numpy as np
import matplotlib.pyplot as plt

# Määritellään uusi kuvaaja-alue
plt.figure(figsize=(6.4*3, 4.8*3))

# Määritellään X-akselin arvot halutulle välille
X = np.linspace(-3*np.pi, 3*np.pi, 256, endpoint=True)

# Lasketaan kosini ja sini -funktioiden arvot
C, S = np.cos(X), np.sin(X)

# Piirretään kuvaajat
plt.plot(X, C, color='red', linestyle='--', label='cosine')  # Punainen katkoviiva
plt.plot(X, S, color='blue', linestyle='-.', label='sine')   # Sininen pisteviiva

# Näytetään selite
plt.legend()

# Asetetaan x- ja y-akseleiden muotoilu
plt.xticks([-3*np.pi, -2*np.pi, -np.pi, 0, np.pi, 2*np.pi, 3*np.pi],
           [r'$-3\pi$', r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$', r'$3\pi$'])

plt.yticks([-1, 0, 1], [r'$-1$', '0', r'$1$'])

# Näytetään kuvaaja
plt.show()
