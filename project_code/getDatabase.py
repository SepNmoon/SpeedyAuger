#connect database

db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='atom_shell',
    charset='utf8'
)

#get atomic number and atomic name
def getAtom():
    cursor = db.cursor()
    sql = 'SELECT * FROM atom'
    cursor.execute(sql)
    results = cursor.fetchall()
    number_name=dict()
    for row in results:
        atom_number = row[0]
        atom_name = row[1]
        number_name[atom_number]=atom_name
    return number_name


#get electron configuration
def getShell():
    cursor = db.cursor()
    sql = 'SELECT * FROM shell'
    cursor.execute(sql)
    results = cursor.fetchall()
    number_shell=dict()
    for row in results:
        temp=dict()
        atom_number = row[0]
        ele_k=row[1]
        ele_l1,ele_l2,ele_l3=row[2],row[3],row[4]
        ele_m1,ele_m2,ele_m3,ele_m4,ele_m5=row[5],row[6],row[7],row[8],row[9]
        ele_n1,ele_n2,ele_n3,ele_n4,ele_n5,ele_n6,ele_n7=row[10],row[11],row[12],row[13],row[14],row[15],row[16]
        ele_o1,ele_o2,ele_o3,ele_o4,ele_o5,ele_o6=row[17],row[18],row[19],row[20],row[21],row[22]
        ele_p1,ele_p2,ele_p3,ele_p4,ele_p5=row[23],row[24],row[25],row[26],row[27]
        ele_q1=row[28]
        temp['K']=ele_k
        temp['L1'],temp['L2'],temp['L3']=ele_l1,ele_l2,ele_l3
        temp['M1'],temp['M2'],temp['M3'],temp['M4'],temp['M5']=ele_m1,ele_m2,ele_m3,ele_m4,ele_m5
        temp['N1'],temp['N2'],temp['N3'],temp['N4'],temp['N5'],temp['N6'],temp['N7']=ele_n1,ele_n2,ele_n3,ele_n4,ele_n5,ele_n6,ele_n7
        temp['O1'],temp['O2'],temp['O3'],temp['O4'],temp['O5'],temp['O6']=ele_o1,ele_o2,ele_o3,ele_o4,ele_o5,ele_o6
        temp['P1'],temp['P2'],temp['P3'],temp['P4'],temp['P5']=ele_p1,ele_p2,ele_p3,ele_p4,ele_p5
        temp['Q1']=ele_q1
        number_shell[atom_number]=temp
    return number_shell


#get electrons energies
def getEnergies():
    cursor = db.cursor()
    sql = 'SELECT * FROM energies'
    cursor.execute(sql)
    results = cursor.fetchall()
    number_energies=dict()
    for row in results:
        temp=dict()
        atom_number = row[0]
        en_k=row[1]
        en_l1,en_l2,en_l3=row[2],row[3],row[4]
        en_m1,en_m2,en_m3,en_m4,en_m5=row[5],row[6],row[7],row[8],row[9]
        en_n1,en_n2,en_n3,en_n4,en_n5,en_n6,en_n7=row[10],row[11],row[12],row[13],row[14],row[15],row[16]
        en_o1,en_o2,en_o3,en_o4,en_o5,en_o6,en_o7=row[17],row[18],row[19],row[20],row[21],row[22],row[23]
        en_p1,en_p2,en_p3,en_p4,en_p5=row[24],row[25],row[26],row[27],row[28]
        en_q1=row[29] 
        temp['K']=en_k
        temp['L1'],temp['L2'],temp['L3']=en_l1,en_l2,en_l3
        temp['M1'],temp['M2'],temp['M3'],temp['M4'],temp['M5']=en_m1,en_m2,en_m3,en_m4,en_m5
        temp['N1'],temp['N2'],temp['N3'],temp['N4'],temp['N5'],temp['N6'],temp['N7']=en_n1,en_n2,en_n3,en_n4,en_n5,en_n6,en_n7
        temp['O1'],temp['O2'],temp['O3'],temp['O4'],temp['O5'],temp['O6'],temp['O7']=en_o1,en_o2,en_o3,en_o4,en_o5,en_o6,en_o7
        temp['P1'],temp['P2'],temp['P3'],temp['P4'],temp['P5']=en_p1,en_p2,en_p3,en_p4,en_p5           
        temp['Q1']=en_q1
        number_energies[atom_number]=temp
    return number_energies


#get barkla and orbital notation
def getNotation():
    cursor = db.cursor()
    sql = 'SELECT * FROM notation'
    cursor.execute(sql)
    results = cursor.fetchall()
    barkla_orbital=dict()
    for row in results:
        barkla_notation = row[0]
        orbital_notation=row[1]
        barkla_orbital[barkla_notation]=orbital_notation   
    return barkla_orbital


def getRange():
    cursor = db.cursor()
    sql = 'SELECT * FROM energies_range'
    cursor.execute(sql)
    results = cursor.fetchall()
    number_range=dict()
    for row in results:
        atom_number=row[0]
        max_value=row[1]
        min_value=row[2]
        temp=dict()
        temp['Max']=max_value
        temp['Min']=min_value
        number_range[atom_number]=temp
    return number_range


if __name__ == "__main__":
    getAtom()
    getShell()
    getEnergies()
    getNotation()
    getRange()
    
    
    
    