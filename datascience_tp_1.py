class Employee:
    def __init__(self, jenis_kelamin, umur, gaji, transportasi):
        self.jenis_kelamin = jenis_kelamin
        self.umur = umur
        self.gaji = gaji
        self.transportasi = transportasi
    
    # Get title based on salary
    def getTitle(self):
        if self.gaji >= 15000000:
            return 'Manager'
        elif self.gaji >= 12000000:
            return 'Asisten Manager'
        elif self.gaji >= 10000000:
            return 'Supervisor'
        else:
            return 'Officer'

# declare employee objects
employees = [
 Employee('Laki - laki', 20, 8000000, 'Kendaraan pribadi'),
 Employee('Laki - laki', 35, 14000000, 'Kendaraan umum'),
 Employee('Perempuan', 26, 10000000, 'Kendaraan umum'),
 Employee('Perempuan', 27, 12000000, 'Kendaraan pribadi'),
 Employee('Laki - laki', 21, 9000000, 'Kendaraan pribadi'),
 Employee('Laki - laki', 22, 11000000, 'Kendaraan pribadi'),
 Employee('Perempuan', 32, 15000000, 'Kendaraan umum'),
 Employee('Perempuan', 26, 8000000, 'Kendaraan umum'),
 Employee('Laki - laki', 25, 9000000, 'Kendaraan umum'),
 Employee('Perempuan', 20, 10000000, 'Kendaraan pribadi'),
]

# Add new function for sorting key
def salaryKey(e):
    return e.gaji

# Sort employee list first
employees.sort(key=salaryKey, reverse=True)

# Printing employees
print("{:<15} {:<5} {:<15} {:<25} {:<15}".format('Jenis kelamin','Umur','Gaji','Transportasi','Jabatan'))

for employee in employees:
    print("{:<15} {:<5} {:<15} {:<25} {:<15}".format(employee.jenis_kelamin,employee.umur,employee.gaji,employee.transportasi,employee.getTitle()))
