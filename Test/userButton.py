import json
import sys
import pyodbc
import BrownieVar as BV
reload(sys)
sys.setdefaultencoding("utf-8")


def keycheck(val, path):
    if val in path:
        return path[val]
    else:
        return 'NULL'


conn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=USE1EDCGBI03;DATABASE=Brownie;Trusted_Connection=True')
cursor = conn.cursor()
cursor.execute('Truncate table brownie..Brownieuserbutton')
cursor.commit()

file=BV.jsonfile
a1 = []
a2=[]
with open (file) as data:
    parse=json.load(data)
    for a in parse['corazon']['accounts']:
        if  parse['corazon']['accounts'][a]['cfg'].get('app','')<>'':
            if parse['corazon']['accounts'][a]['cfg']['app'].get('created','')<>'':
                
                created=str(parse['corazon']['accounts'][a]['cfg']['app']['created'])
            else:
                created='NULL'
                
            if parse['corazon']['accounts'][a].get('cfg','')<>'' and parse['corazon']['accounts'][a]['cfg']['app'].get('buttons','')<>'':
                for buttonid in parse['corazon']['accounts'][a]['cfg']['app']['buttons']: 
                    accountid="'"+a+"'"
                    Buttonid="'"+buttonid+"'"
                    unitId="'"+keycheck('unitId',parse['corazon']['accounts'][a]['cfg']['app']['buttons'][buttonid]['info'])+"'"
                    name="'"+keycheck('name',parse['corazon']['accounts'][a]['cfg']['app']['buttons'][buttonid]).replace("'","''")+"'"
                    status="'"+str(keycheck('status',parse['corazon']['accounts'][a]['cfg']['app']['buttons'][buttonid])).replace("'","''")+"'"
                    colour=keycheck('color',parse['corazon']['accounts'][a]['cfg']['app']['buttons'][buttonid]['info'])
                    skinId="'"+str(keycheck('skinId',parse['corazon']['accounts'][a]['cfg']['app']['buttons'][buttonid]['info']))+"'"
                    hw="'"+keycheck('hw',parse['corazon']['accounts'][a]['cfg']['app']['buttons'][buttonid]['info'])+"'"
                    kit="'"+keycheck('eco',parse['corazon']['accounts'][a]['cfg']['app']['buttons'][buttonid])+"'"
                    
                    k=("""Insert into Brownieuserbutton(Accountid,Buttonid,Unitid,Name,Status,colour,skinid,HW,Created,kit)values("""+accountid+','+Buttonid+','+unitId+','+name+','+status+','+str(colour)+','+skinId+','+hw+','+created+','+kit+')')
                    #print k
                    cursor.execute("""Insert into Brownieuserbutton(Accountid,Buttonid,Unitid,Name,Status,colour,skinid,HW,Created,kit)values("""+accountid+','+Buttonid+','+unitId+','+name+','+status+','+str(colour)+','+skinId+','+hw+','+created+','+kit+')')
                    cursor.commit()
                    #print a
print 'User button done'

          
