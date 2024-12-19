import lines
import pandas
import folium

d = {'NBAA': 'Shaheed Sthal-New Bus Adda', 'HDNR': 'Hindon River', 'ATHA': 'Arthala', 'MNGM': 'Mohan Nagar', 'SMPK': 'Shyam Park', 'RJNM': 'Maj M.Sharma-Rajendra Nagar', 'RJBH': 'Raj Bagh', 'SHDN': 'Shahid Nagar', 'DSG': 'Dilshad Garden', 'JLML': 'Jhilmil', 'MPK': 'Mansarovar Park', 'SHD': 'Shahdara', 'WC': 'Welcome', 'SLAP': 'Seelampur', 'SHPK': 'Shastri Park', 'KGR': 'Kashmere Gate', 'TZI': 'Tis Hazari', 'PBGH': 'Pul Bangash', 'PRA': 'Pratap Nagar', 'SHT': 'Shastri Nagar', 'ILOK': 'Inderlok', 'KN': 'Kanhaiya Nagar', 'KP': 'Keshav Puram', 'NSHP': 'Netaji Subhash Place', 'KE': 'Kohat Enclave', 'PTP': 'Pitampura', 'RHE': 'Rohini East', 'RHW': 'Rohini West', 'RI': 'Rithala', 'SPBI': 'Samaypur Badli', 'RISE': 'RohiniSE18', 'BIMR': 'Haider Pur', 'JGPI': 'Jahangir Puri', 'AHNR': 'Adarsh Nagar', 'AZU': 'Azadpur', 'MDTW': 'Model Town', 'GTBR': 'GTB Nagar', 'VW': 'Vishwa Vidalaya', 'VS': 'Vidhan Sabha', 'CL': 'Civil Lines', 'KGM': 'Kashmere Gate', 'CHK': 'Chandni Chowk', 'CWBR': 'Chawri Bazar', 'NDI': 'New Delhi', 'RCK': 'Rajiv Chowk', 'PTCK': 'Patel Chowk', 'CTST': 'Central Secretariat', 'UDB': 'Udyog Bhavan', 'RCC': 'Race Course', 'JB': 'Jor Bagh', 'INA': 'INA', 'AIIM': 'AIIMS', 'GNPK': 'Green Park', 'HKS': 'Hauzkhas', 'MVNR': 'Malaviya Nagar', 'SAKT': 'Saket', 'QM': 'Qutab Minar', 'CHTP': 'Chhatar Pur', 'SLTP': 'Sultan Pur', 'GTNI': 'Ghitorny', 'AJG': 'Arjan Garh', 'GE': 'Guru DronaCharya', 'SKRP': 'Sikanderpur', 'MGRO': 'MG Road', 'IFOC': 'Iffco Chowk', 'HCC': 'Huda City Centre', 'VASI': 'Vaishali', 'KASI': 'Kaushambi', 'AVIT': 'Anand Vihar ISBT', 'KKDA': 'Karkardooma', 'PTVR': 'Preet Vihar', 'NV': 'Nirman Vihar', 'LN': 'Laxmi Nagar', 'NECC': 'Noida Electronic City', 'SSTN': 'Sector-62 Noida', 'SFNN': 'Sector-59 Noida', 'SSON': 'Sector-61 Noida', 'SFTN': 'Sector-52 Noida', 'STFN': 'Sector-34 Noida', 'NCC': 'Noida City Center', 'GEC': 'Golf Course', 'BCGN': 'Botanical Garden L-8', 'NSET': 'Noida Sec18', 'NSST': 'Noida Sec16', 'NSFT': 'Noida Sec15', 'NAKR': 'New Ashok Nagar', 'MVPE': 'Mayur VPH1E', 'MVP1': 'Mayur VPH1', 'ASDM': 'Akshardham', 'YB': 'Yamuna Bank', 'IDPT': 'Indraprastha', 'PTMD': 'Pragati Maidan', 'MDHS': 'Mandi House', 'BRKR': 'Barakhamba Road', 'RKAM': 'R K Ashram', 'JW': 'Jhandewalan', 'KB': 'Karol Bagh', 'RP': 'Rajendra Place', 'PN': 'Patel Nagar', 'SP': 'Shadipur', 'KNR.': 'Kirti Nagar', 'MN': 'Moti Nagar', 'RN': 'Ramesh Nagar', 'RG': 'Rajouri Garden', 'TG': 'Tagore Garden', 'SN': 'Subhash Nagar', 'TN': 'Tilak Nagar', 'JPE': 'Janak Puri E', 'JPW': 'Janak Puri W', 'UNE': 'Uttam Ngr E', 'UNW': 'Uttam Ngr W', 'NWD': 'Nawada', 'DM': 'Dwarka Mor', 'DW': 'Dwarka', 'DSFN': 'Dwarka SE14', 'DSTN': 'Dwarka SE13', 'DSW': 'Dwarka SE12', 'DSE': 'Dwarka SE11', 'DST': 'Dwarka SE10', 'DSN': 'Dwarka SE09', 'DWET': 'Dwarka Sec08', 'DWTO': 'Dwarka Sec21', 'KNR-5': 'Kirti Nagar', 'SRSM': 'Sat Guru Ram Singh', 'ILOK- N': 'Inderlok', 'APMN': 'Ashok Park Main', 'PBGA': 'Punjabi Bagh', 'SHVP': 'Shivaji Park', 'MAPR': 'Madi Pur', 'PVE': 'Paschim V E', 'PVW': 'Paschim V W', 'PAGI': 'Peera Garhi', 'UNRG': 'Udyog Nagar', 'SMSM': 'Surajmal Stadium', 'NNOI': 'Nangloi', 'NRSN': 'Nangloi Railway Station', 'RDPK': 'Rajdhani Park', 'MUDK': 'Mundka', 'MIAA': 'Mundka IA', 'GHEM': 'Ghevra', 'TKLM': 'Tikri Kalan', 'TKBR': 'Tikri Border', 'MIEE': 'Modern Industrial Estate', 'BUSS': 'Bus Stand', 'CIPK': 'City Park', 'KG-6': 'Kashmere Gate', 'LLQA': 'Lal Quila', 'JAMD': 'Jama Masjid', 'DLIG': 'Delhi Gate', 'IT0': 'ITO', 'MDHS-6': 'Mandi House', 'JANP': 'Janpath', 'CTST-N': 'Central Secretariat', 'KM': 'Khan Market', 'JLNS': 'JLN Stadium', 'JGPA': 'Jangpura', 'LJPN': 'Lajpat Nagar', 'MLCD': 'Moolchand', 'KHCY': 'Kailash Colony', 'NP': 'Nehru Place', 'KJMD-8': 'Kalkaji Mandir', 'GDPI': 'Gobind Puri', 'OK': 'Harkesh Nagar Okhla', 'JLA': 'Jasola Apollo', 'STVR': 'Sarita Vihar', 'METE': 'Mohan Estate', 'TKBD': 'Tughlakabad', 'BAPU': 'Badarpur', 'SRAI': 'Sarai', 'NHPC': 'NHPC Chowk', 'NMJR': 'Mewala Maharajpur', 'FTTA': 'Sector 28', 'BKMR': 'Badkal Mor', 'OFDB': 'Faridabad Old', 'NCAJ': 'Neelam Chowk Ajronda', 'BACH': 'Bata Chowk', 'ECMJ': 'Escorts Mujesar', 'NCBC': 'Sant Surdas Sihi', 'BYHM': 'Raja Nahar Singh', 'MKPR': 'Majlis Park', 'AZU-7': 'Azadpur', 'SMBG': 'Shalimar Bagh', 'NSHP-7': 'Netaji Subhash Place', 'SAKP': 'Shakurpur', 'PBGW': 'Punjabi Bagh West', 'ESIH': 'ESI Hospital', 'RG-7': 'Rajouri Garden L-7', 'MYPI': 'Mayapuri', 'NAVR': 'Naraina Vihar', 'DLIC': 'Delhi Cantt', 'DDSC': 'DD South Campus', 'SVMB': 'SV Moti Bagh', 'BKCP': 'Bhikaji Cama Place', 'SOJI': 'Sarojini Nagar', 'INA-7': 'INA', 'SOEN': 'South Extension', 'LJPN-7': 'Lajpat Nagar', 'VNPR': 'Vinobapuri', 'AHRM': 'Ashram', 'NIZM': 'Hazrat Nizamuddin', 'MVPI': 'Mayur VPH1', 'MVPO': 'Mayur VPKT1', 'TKPR': 'Trilokpuri', 'VENT': 'East Vinod Nagar', 'VNNR': 'Mandawali-West Vinod Nagar', 'IPE': 'IP Extension', 'AVIT-7': 'Anand Vihar ISBT', 'KKDC': 'Karkardooma', 'KHNA': 'Krishna Nagar', 'EANR': 'East Azad Nagar', 'WC-7': 'Welcome', 'JFRB': 'Jaffrabad', 'MUPR': 'Maujpur', 'GKPR': 'Gokulpuri', 'JIEE': 'Johri Enclave', 'SVVR': 'Shiv Vihar', 'BCGN-8': 'Botanical Garden L-8', 'OBC': 'Okhla Bird Sanctuary', 'KIKJ': 'Kalindi Kunj', 'JLA-8': 'Jasola Vihar Shaheen Bagh', 'OVA': 'Okhla Vihar', 'JANR': 'Jamia Millia Islamia', 'IWNR': 'Sukhdev Vihar', 'OKNS': 'Okhla NSIC', 'NUEE': 'Nehru Enclave', 'GKEI': 'G.K.Enclave-I', 'CDLI': 'Chirag Delhi', 'PSPK': 'Panchsheel Park', 'HKS-8': 'Hauzkhas', 'IIT': 'IIT', 'RKPM': 'R.K. Puram', 'MIRK': 'Munirka', 'VTVR': 'Vasant Vihar', 'SKVR': 'Shankar Vihar', 'IGDA': 'IGD Airport', 'SABR': 'Sadar Bazar', 'PALM': 'PALAM', 'DSHP': 'Dashrathpuri', 'DBMR': 'Dabri Mor', 'JPW-8': 'Janakpuri West L-8', 'Sector 55-56': 'Sector 55-56', 'Sector 54 Chowk': 'Sector 54 Chowk', 'Sector 53-54': 'Sector 53-54', 'Sector 42-43': 'Sector 42-43', 'Phase 1': 'Phase 1', 'Sikanderpur': 'Sikanderpur', 'Phase 2': 'PHASE 2', 'Belvedere Towers': 'Belvedere Towers', 'Cyber City': 'Cyber City', 'Moulsari Avenue': 'Moulsari Avenue', 'Phase 3': 'PHASE 3'}


red_interchanges = {'pink' : 'Welcome', 'violet' : "Kashmere Gate", "yellow" : "Kashmere Gate", "green" : "Inderlok", "pink_" : "Netaji Subhash Place"}

yellow_interchanges = {"pink" : "Azadpur", "red" : "Kashmere Gate", "violet" : "Kashmere Gate", "blue3" : "Rajiv Chowk", "violet" : "Central Secretariat", "pink_" : "INA", "magenta" : "Hauzkhas"}

blue3_interchanges = {"magenta" : "Janakpuri West", "pink" : "Rajouri Garden", "green" : "Kirti Nagar", "yellow"  : "Rajiv Chowk", "violet" : "Mandi House", "pink_" : "Mayur Vihar 1", "magenta" : "Botanical Garden L-8"}

blue4_interchanges = {"pink" : "Karkardooma", "pink_" : "Anand Vihar ISBT"}

green_interchanges = {"red" : "Inderlok", "pink" : "Punjabi Bagh West", "blue3" : "Kirti Nagar"}

violet_interchanges = {"red" : "Kashmere Gate", "blue3" : "Mandi House", "yellow" : "Central Secretariat", "pink" : "Lajpat Nagar", "magenta" : "Kalkaji Mandir"}

pink_interchanges = {"yellow" : "Azadpur", "red" : "Netaji Subhash Place", "green" : "Punjabi Bagh West", "blue3" : "Rajouri Garden", "yellow_" : "INA", "violet" : "Lajpat Nagar", "blue3" : "Mayur Vihar 1", "blue4" : "Anand Vihar ISBT", "blue4_" : "Karkardooma", "red" : "Welcome"}

magenta_interchanges = {"blue3" : "Janakpuri West", "yellow" : "Hauzkhas", "violet" : "Kalkaji Mandir", "blue3" : "Botanical Garden L-8"}

# delhi_metro_coordinates = {
#     "Shahdara": (28.6733, 77.2895),
#     "Welcome": (28.6692, 77.2825),
#     "Seelampur": (28.6660, 77.2770),
#     "Shastri Park": (28.6615, 77.2580),
#     "Kashmere Gate": (28.6670, 77.2274),
#     "Tis Hazari": (28.6625, 77.2167),
#     "Pul Bangash": (28.6585, 77.2100),
#     "Pratap Nagar": (28.6570, 77.2025),
#     "Shastri Nagar": (28.6620, 77.1945),
#     "Inderlok": (28.6690, 77.1870),
#     "Kanhaiya Nagar": (28.6880, 77.1805),
#     "Keshav Puram": (28.6965, 77.1725),
#     "Netaji Subhash Place": (28.6930, 77.1510),
#     "Kohat Enclave": (28.6960, 77.1405),
#     "Pitampura": (28.7005, 77.1325),
#     "Rohini East": (28.7170, 77.1270),
#     "Rohini West": (28.7215, 77.1175),
#     "Rithala": (28.7295, 77.1100),
#     "Mansarovar Park": (28.6825, 77.3070),
#     "Jhilmil": (28.6745, 77.3060),
#     "Dilshad Garden": (28.6740, 77.3020),
#     "Shahid Nagar": (28.6725, 77.2955),
#     "Raj Bagh": (28.6710, 77.2890),
#     "Maj M.Sharma-Rajendra Nagar": (28.6695, 77.2825),
#     "Shyam Park": (28.6680, 77.2760),
#     "Mohan Nagar": (28.6665, 77.2695),
#     "Arthala": (28.6650, 77.2630),
#     "Hindon River": (28.6635, 77.2565),
#     "Shaheed Sthal-New Bus Adda": (28.6620, 77.2500),
#     "Vishwa Vidalaya": (28.6910, 77.2145),
#     "Vidhan Sabha": (28.6815, 77.2130),
#     "Civil Lines": (28.6740, 77.2225),
#     "Chandni Chowk": (28.6560, 77.2300),
#     "Chawri Bazar": (28.6505, 77.2325),
#     "New Delhi": (28.6422, 77.2215),
#     "Rajiv Chowk": (28.6328, 77.2197),
#     "Patel Chowk": (28.6265, 77.2135),
#     "Central Secretariat": (28.6172, 77.2080),
#     "Jahangir Puri": (28.7255, 77.1855),
#     "Adarsh Nagar": (28.7164, 77.1705),
#     "Azadpur": (28.7075, 77.1660),
#     "Model Town": (28.7029, 77.1937),
#     "GTB Nagar": (28.6935, 77.2040),
#     "Udyog Bhavan": (28.6115, 77.2085),
#     "Race Course": (28.6015, 77.2070),
#     "Jor Bagh": (28.5925, 77.2075),
#     "INA": (28.5845, 77.2070),
#     "AIIMS": (28.5670, 77.2070),
#     "Green Park": (28.5535, 77.2070),
#     "Saket": (28.5225, 77.2060),
#     "Qutab Minar": (28.5145, 77.1985),
#     # "Chhatarpur": (28.5025, 77.1765),
#     # "Sultanpur": (28.4965, 77.1675),
#     "Ghitorny": (28.4938, 77.1492),
#     "Arjan Garh": (28.4825, 77.1345),
#     "Guru DronaCharya": (28.4795, 77.1125),
#     "Sikanderpur": (28.4815, 77.1005),
#     "MG Road": (28.4795, 77.0885),
#     "Iffco Chowk": (28.4745, 77.0705),
#     "Huda City Centre": (28.4595, 77.0725),
#     "Haider Pur": (28.7215, 77.1575),
#     "RohiniSE18": (28.7345, 77.1245),
#     "Samaypur Badli": (28.7446, 77.1383),
#     "Indraprastha": (28.6205, 77.2425),
#     "Pragati Maidan": (28.6235, 77.2415),
#     "Mandi House": (28.6275, 77.2345),
#     "Barakhamba Road": (28.6315, 77.2215),
#     "R K Ashram": (28.6395, 77.2105),
#     "Jhandewalan": (28.6465, 77.2025),
#     "Karol Bagh": (28.6535, 77.1935),
#     "Rajendra Place": (28.6585, 77.1855),
#     "Patel Nagar": (28.6625, 77.1775),
#     "Shadipur": (28.6665, 77.1695),
#     "Moti Nagar": (28.6705, 77.1615),
#     "Ramesh Nagar": (28.6745, 77.1535),
#     "Rajouri Garden": (28.6795, 77.1455),
#     "Tagore Garden": (28.6835, 77.1375),
#     "Subhash Nagar": (28.6875, 77.1295),
#     "Tilak Nagar": (28.6425, 77.0890),
#     "Janak Puri E": (28.6294, 77.0867),
#     "Janak Puri W": (28.6294, 77.0777),
#     "Uttam Ngr E": (28.6215, 77.0755),
#     "Uttam Ngr W": (28.6215, 77.0655),
#     "Nawada": (28.6215, 77.0555),
#     "Dwarka Mor": (28.6215, 77.0455),
#     "Dwarka": (28.6215, 77.0355),
#     "Dwarka SE14": (28.6215, 77.0255),
#     "Dwarka SE13": (28.6215, 77.0155),
#     "Dwarka SE12": (28.6215, 77.0055),
#     "Dwarka SE11": (28.6215, 76.9955),
#     "Dwarka SE10": (28.6215, 76.9855),
#     "Dwarka SE09": (28.6215, 76.9755),
#     "Yamuna Bank": (28.6205, 77.2735),
#     "Akshardham": (28.6185, 77.2775),
#     "Mayur VPH1": (28.6045, 77.2895),
#     "Mayur VPH1E": (28.5945, 77.2945),
#     "New Ashok Nagar": (28.5905, 77.3025),
#     "Noida Sec15": (28.5865, 77.3185),
#     "Noida Sec16": (28.5835, 77.3265),
#     "Noida Sec18": (28.5705, 77.3265),
#     "Golf Course": (28.5675, 77.3345),
#     "City Centre": (28.5705, 77.3425),
#     "Dwarka Sec08": (28.5658, 77.0671),
#     "Dwarka Sec21": (28.5485, 77.0555),
#     "Sector-34 Noida": (28.5705, 77.3505),
#     "Sector-52 Noida": (28.5835, 77.3625),
#     "Sector-61 Noida": (28.5905, 77.3705),
#     "Sector-59 Noida": (28.5905, 77.3785),
#     "Sector-62 Noida": (28.5905, 77.3865),
#     "Noida Electronic City": (28.5905, 77.3945),
#     "Karkardooma": (28.6485, 77.3055),
#     "Preet Vihar": (28.6375, 77.2905),
#     "Nirman Vihar": (28.6315, 77.2825),
#     "Laxmi Nagar": (28.6306, 77.2775),
#     "Kaushambi": (28.6454, 77.3243),
#     "Vaishali": (28.6475, 77.3385),
#     "Ashok Park Main": (28.6785, 77.1545),
#     "Punjabi Bagh": (28.6729, 77.1461),
#     "Shivaji Park": (28.6785, 77.1385),
#     "Madi Pur": (28.6773, 77.1196),
#     "Paschim V W": (28.6785, 77.1023),
#     "Paschim V E": (28.6785, 77.1103),
#     "Peera Garhi": (28.6785, 77.0943),
#     "Udyog Nagar": (28.6785, 77.0863),
#     "Surajmal Stadium": (28.6785, 77.0783),
#     "Nangloi": (28.6785, 77.0703),
#     "Nangloi Railway Station": (28.6785, 77.0623),
#     "Rajdhani Park": (28.6785, 77.0543),
#     "Mundka": (28.6785, 77.0463),
#     "Sat Guru Ram Singh": (28.6785, 77.0383),
#     "Kirti Nagar": (28.6558, 77.1506),
#     "Mundka IA": (28.6785, 77.0303),
#     "Ghevra": (28.6785, 77.0223),
#     "Tikri Kalan": (28.6785, 77.0143),
#     "Tikri Border": (28.6785, 77.0063),
#     "Modern Industrial Estate": (28.6785, 76.9983),
#     "Bus Stand": (28.6785, 76.9903),
#     "City Park": (28.6785, 76.9823),
#     "Central Secretariat": (28.6172, 77.2080),
#     "Khan Market": (28.6028, 77.2283),
#     "JLN Stadium": (28.5904, 77.2333),
#     "Jangpura": (28.5843, 77.2377),
#     "Lajpat Nagar": (28.5708, 77.2365),
#     "Moolchand": (28.5585, 77.2345),
#     "Kailash Colony": (28.5553, 77.2421),
#     "Nehru Place": (28.5495, 77.2515),
#     "Kalkaji Mandir": (28.5483, 77.2583),
#     "Gobind Puri": (28.5445, 77.2640),
#     "Harkesh Nagar Okhla": (28.5295, 77.2695),
#     "Jasola Vihar Shaheen Bagh": (28.5405, 77.2905),#**
#     "Sarita Vihar": (28.5405, 77.3025),
#     "Mohan Estate": (28.5405, 77.3145),
#     "Tughlakabad": (28.5105, 77.3105),
#     "Badarpur": (28.4945, 77.3025),
#     "Janpath": (28.6275, 77.2165),
#     "ITO": (28.6285, 77.2425),
#     "Sarai": (28.4595, 77.2995),
#     "NHPC Chowk": (28.4495, 77.3005),
#     "Mewala Maharajpur": (28.4395, 77.3005),
#     "Sector 28": (28.4295, 77.3005),
#     "Badkal Mor": (28.4195, 77.3005),
#     "Faridabad Old": (28.4095, 77.3005),
#     "Neelam Chowk Ajronda": (28.3995, 77.3005),
#     "Bata Chowk": (28.3895, 77.3005),
#     "Escorts Mujesar": (28.3795, 77.3005),
#     "Delhi Gate": (28.6415, 77.2425),
#     "Jama Masjid": (28.6505, 77.2345),
#     "Lal Quila": (28.6565, 77.2315),
#     "Kashmere Gate": (28.6675, 77.2282),
#     "Sant Surdas Sihi": (28.3695, 77.3005),
#     "Raja Nahar Singh": (28.3595, 77.3005),
#     "Welcome": (28.6745, 77.2835),
#     "Anand Vihar ISBT": (28.6465, 77.3155),
#     "Karkardooma": (28.6485, 77.3055),
#     "Mayur VPH1": (28.6045, 77.2895),
#     "INA": (28.5753, 77.2094),
#     "Lajpat Nagar": (28.5708, 77.2365),
#     "Majlis Park": (28.7165, 77.1855),
#     "Azadpur": (28.7072, 77.1806),
#     "Shalimar Bagh": (28.7025, 77.1735),
#     "Netaji Subhash Place": (28.6965, 77.1495),
#     "Shakurpur": (28.6905, 77.1395),
#     "Punjabi Bagh West": (28.6805, 77.1295),
#     "ESI Hospital": (28.6705, 77.1195),
#     "Rajouri Garden": (28.6635, 77.1105),
#     "Mayapuri": (28.6545, 77.1005),
#     "Naraina Vihar": (28.6455, 77.0905),
#     "Delhi Cantt": (28.6365, 77.0805),
#     "DD South Campus": (28.6275, 77.0705),
#     "SV Moti Bagh": (28.6185, 77.0605),
#     "Bhikaji Cama Place": (28.6095, 77.0505),
#     "Sarojini Nagar": (28.6005, 77.0405),
#     "South Extension": (28.5915, 77.0305),
#     "Vinobapuri": (28.5825, 77.0205),
#     "Ashram": (28.5735, 77.0105),
#     "Hazrat Nizamuddin": (28.5645, 77.0005),
#     "Mayur VPKT1": (28.6045, 77.2895),
#     "Trilokpuri": (28.5955, 77.2795),
#     "East Vinod Nagar": (28.5865, 77.2695),
#     "Mandawali-West Vinod Nagar": (28.5775, 77.2595),
#     "IP Extension": (28.5685, 77.2495),
#     "Karkardooma": (28.5595, 77.2395),
#     "Krishna Nagar": (28.5505, 77.2295),
#     "East Azad Nagar": (28.5415, 77.2195),
#     "Jaffrabad": (28.5325, 77.2095),
#     "Maujpur": (28.5235, 77.1995),
#     "Gokulpuri": (28.5145, 77.1895),
#     "Johri Enclave": (28.5055, 77.1795),
#     "Shiv Vihar": (28.4965, 77.1695),
#     "Hauzkhas": (28.5495, 77.2067),
#     "Botanical Garden L-8": (28.5645, 77.3265),
#     "Okhla Bird Sanctuary": (28.5545, 77.3165),
#     "Kalindi Kunj": (28.5445, 77.3065),
#     "Jasola Vihar Shaheen Bagh": (28.5345, 77.2965),
#     "Okhla Vihar": (28.5245, 77.2865),
#     "Jamia Millia Islamia": (28.5145, 77.2765),
#     "Sukhdev Vihar": (28.5613, 77.2757),
#     "Okhla NSIC": (28.5550, 77.2660),
#     "Kalkaji Mandir": (28.5483, 77.2583),
#     "Nehru Enclave": (28.5410, 77.2560),
#     "G.K.Enclave-I": (28.5350, 77.2430),
#     "Chirag Delhi": (28.5270, 77.2340),
#     "Panchsheel Park": (28.5220, 77.2240),
#     "IIT": (28.5450, 77.1920),
#     "R.K. Puram": (28.5540, 77.1870),
#     "Munirka": (28.5580, 77.1730),
#     "Vasant Vihar": (28.5660, 77.1620),
#     "Shankar Vihar": (28.5640, 77.1500),
#     "IGD Airport": (28.5569, 77.0867),
#     "Sadar Bazar": (28.6690, 77.2200),
#     "PALAM": (28.5800, 77.1250),
#     "Dashrathpuri": (28.5890, 77.1100),
#     "Dabri Mor": (28.5950, 77.1000),
#     "Janakpuri West L-8": (28.6294, 77.0777),
#     "Dwarka": (28.6080, 77.0400),
#     "Sikanderpur": (28.4810, 77.0840),
#     "PHASE 2": (28.4740, 77.0800),
#     "Belvedere Towers": (28.4710, 77.0760),
#     "Cyber City": (28.4790, 77.0720),
#     "Moulsari Avenue": (28.4830, 77.0680),
#     "PHASE 3": (28.4870, 77.0640),
#     "Phase 1": (28.4900, 77.0600),
#     "Sector 42-43": (28.4950, 77.0560),
#     "Sector 53-54": (28.5000, 77.0520),
#     "Sector 54 Chowk": (28.5050, 77.0480),
#     "Sector 55-56": (28.5100, 77.0440),
#     "Malaviya Nagar": (28.5286, 77.2033),
#     "Chhatar Pur": (28.4530, 77.1490),
#     "Sultan Pur": (28.4530, 77.1490),
#     # "Chhatarpur": (28.5025, 77.1765),
#     # "Sultanpur": (28.4965, 77.1675),
#     "Noida City Center": (28.5720, 77.3200),
#     "Gobind Puri": (28.5530, 77.2900),
#     "Jasola Apollo": (28.5530, 77.2900),
#     "Mayur VPKT1": (28.5530, 77.2900)}
 
# print(len(d))
# print(len(delhi_metro_coordinates))

# for i in d.values():
#     if i not in delhi_metro_coordinates.keys():
#         print(i)


# s1 = set(d.values())
# s2 = set(delhi_metro_coordinates.keys())

# print(len(s1), len(s2))

# print(s2 - s1)

# m = folium.Map(location=delhi_metro_coordinates[list(delhi_metro_coordinates)[0]], zoom_start= 5)

# for i in delhi_metro_coordinates:
#     if i in lines.yellow_line2:
#         folium.Marker(delhi_metro_coordinates[i], popup=f"{i}", icon=folium.Icon(color = "yellow")).add_to(m)

# m.save("maps__.html")




# f = open("DMRC_GTFS/stops.txt", 'r')

# coordinates = {}

# for i in f.readlines():
#     print(i)
#     if i.split(',,')[1] in d.values():
#         coordinates[i.split(',,')[1]] = tuple(map(float, i.split(',,')[2].split(',')))
#     else:
#         coordinates[i.split(',,')[1]] = tuple(map(float, i.split(',,')[2].split(',')))


# print(coordinates)

coordinates = {'Shaheed Sthal-New Bus Adda': (28.670177, 77.416031), 'Hindon River': (28.673508, 77.40654), 'Arthala': (28.6772, 77.391876), 'Mohan Nagar': (28.67856, 77.384209), 'Shyam Park': (28.678217, 77.370911), 'Maj M.Sharma-Rajendra Nagar': (28.678095, 77.359528), 'Raj Bagh': (28.677122, 77.346466), 'Shahid Nagar': (28.676615, 77.333809), 'Dilshad Garden': (28.675991, 77.321495), 'Jhilmil': (28.675648, 77.312393), 'Mansarovar Park': (28.675352, 77.301178), 'Shahdara': (28.673531, 77.28727), 'Welcome': (28.671986, 77.277931), 'Seelampur': (28.670324, 77.267311), 'Shastri Park': (28.668451, 77.250404), 'Kashmere Gate': (28.667879, 77.228012), 'Tis Hazari': (28.667137, 77.216721), 'Pul Bangash': (28.66571, 77.206329), 'Pratap Nagar': (28.666632, 77.196869), 'Shastri Nagar': (28.670135, 77.181679), 'Inderlok': (28.673452, 77.170235), 'Kanhaiya Nagar': (28.682386, 77.162552), 'Keshav Puram': (28.688944, 77.161774), 'Netaji Subash Place': (28.695637, 77.152428), 'Kohat Enclave': (28.697943, 77.140465), 'Pitampura': (28.70318, 77.132355), 'Rohini East': (28.707941, 77.125732), 'Rohini West': (28.715008, 77.115746), 'Rithala': (28.720821, 77.105042), 'Mundka': (28.682411, 77.028282), 'Rajdhani Park': (28.682217, 77.043869), 'Nangloi Railway Station': (28.682091, 77.05619), 'Nangloi': (28.682356, 77.064728), 'Maharaja Surajmal Stadium': (28.681833, 77.073891), 'Udyog Nagar': (28.681047, 77.078674), 'Peera Garhi': (28.67972, 77.092491), 'Paschim V W': (28.678539, 77.102119), 'Paschim V E': (28.677305, 77.112251), 'Madi Pur': (28.676418, 77.117294), 'Shivaji Park': 
(28.674965, 77.128258), 'Punjabi Bagh': (28.672943, 77.146011), 'Ashok Park Main': (28.671572, 77.155159), 'Satguru Ram Singh Marg': (28.662188, 77.157829), 'Samaypur Badli': (28.742872, 77.146545), 'RohiniSE18': (28.740192, 77.135574), 'Haider Pur': (28.718657, 77.149956), 'Jahangir Puri': (28.72818, 77.16124), 'Adarsh Nagar': (28.696377, 77.208809), 'Azadpur': (28.707287, 77.179863), 'Model Town': (28.702833, 77.193764), 'GTB Nagar': (28.698195, 77.206985), 'Vishwa Vidyalaya': (28.694765, 77.212418), 'Vidhan Sabha': (28.687845, 77.221626), 'Civil Lines': (28.676945, 77.224953), 'Chandni Chowk': (28.656443, 77.229218), 'Chawri Bazar': (28.649635, 77.22628), 'New Delhi': (28.642944, 77.222351), 'Rajiv Chowk': (28.632896, 77.219574), 'Patel Chowk': (28.622967, 77.212288), 'Central Secretariat': (28.614973, 77.212029), 'Udyog Bhawan': (28.611525, 77.210052), 'Lok Kalyan Marg': (28.597519, 77.209122), 'Jor Bagh': (28.587234, 77.212662), 'INA': (28.575195, 77.209473), 'AIIMS': (28.568199, 77.207947), 'Green Park': (28.559853, 77.206902), 'Hauzkhas': (28.543346, 77.206673), 'Malaviya Nagar': (28.52817, 77.205612), 'Saket': (28.520638, 77.199379), 'Qutab Minar': (28.512714, 77.185791), 'Chhattar Pur': (28.506584, 77.174866), 'Sultan Pur': (28.499214, 77.161362), 'Ghitorny': (28.49383, 77.149071), 'Arjan Garh': (28.48082, 77.12587), 'Guru DronaCharya': (28.482075, 77.102219), 'Sikanderpur': (28.481352, 77.092995), 'MG Road': (28.47967, 77.080444), 'Iffco Chowk': (28.472137, 77.072502), 'Huda City Centre': (28.459118, 77.072586), 'Vaishali': (28.650059, 77.337608), 'Kaushambi': (28.645428, 77.322273), 'Anand Vihar ISBT': (28.647005, 77.316185), 'Karkardooma': (28.648653, 77.304581), 'Preet Vihar': (28.641352, 77.295158), 'Nirman Vihar': (28.637049, 77.287872), 'Laxmi Nagar': (28.629843, 77.276428), 'Noida City Centre': (28.574593, 77.356117), 'Golf Course': (28.566917, 77.345726), 'Botanical Garden L-8': (28.564198, 77.334656), 'Noida Sec18': (28.570843, 77.326088), 'Noida Sec16': (28.577921, 77.318115), 'Noida Sec15': (28.585018, 77.311584), 'New Ashok Nagar': (28.58847, 77.30146), 'Mayur VPH1E ': (28.594124, 77.294495), 'Mayur VPH1': (28.604425, 77.289421), 'Akshardham': (28.618364, 77.279816), 'Yamuna Bank': (28.623178, 77.267937), 'Indraprastha': (28.620272, 77.250076), 'Supreme Court': (28.623438, 77.2425), 'Mandi House': (28.625816, 77.234726), 'Barakhamba Road': (28.629662, 77.224876), 'R K Ashram': (28.639217, 77.206291), 'Jhandewalan': (28.644312, 77.199791), 'Karol Bagh': (28.643925, 77.188416), 'Rajendra Place': (28.64241, 77.191833), 'Patel Nagar': (28.645037, 77.167046), 'Shadipur': (28.65143, 77.156021), 'Kirti Nagar': (28.655773, 77.148499), 'Moti Nagar': (28.657803, 77.140488), 'Ramesh Nagar': (28.652809, 77.131462), 'Rajouri Garden': (28.649157, 77.122749), 'Tagore Garden': (28.643795, 77.112747), 'Subhash Nagar': (28.640381, 77.10273), 'Tilak Nagar': (28.636568, 77.096336), 'Janak Puri E': (28.633121, 77.086578), 'Janak Puri W': (28.629637, 77.077866), 'Uttam Ngr E': (28.624643, 77.063126), 'Uttam Ngr W': (28.621672, 77.055664), 'Nawada': (28.620222, 77.044991), 'Dwarka Mor': (28.619366, 77.033188), 'Dwarka': (28.614899, 77.022629), 'Dwarka SE14': (28.602232, 77.02594), 'Dwarka SE13': (28.59705, 77.033043), 'Dwarka SE2': (28.592234, 77.040558), 'Dwarka SE11': (28.58642, 77.049255), 'Dwarka SE10': (28.581108, 77.05719), 'Dwarka SE09': (28.574284, 77.065086), 'Dwarka SE08': (28.565706, 77.064896), 'Dwarka Sec21': (28.552322, 77.056198), 'ITO': (28.627205, 77.240952), 'Janpath': (28.627817, 77.218956), 'Khan Market': (28.602682, 77.228096), 'JLN Stadium': (28.590475, 77.23307), 'Jangpura': (28.583231, 77.239662), 'Lajpat Nagar': (28.570705, 77.233124), 'Moolchand': (28.564629, 77.234222), 'Kailash Colony': (28.554617, 77.239738), 'Nehru Place': (28.551134, 77.251511), 'Kalkaji Mandir': (28.549532, 77.258789), 'Gobind Puri': (28.544413, 77.264259), 'Harkesh Nagar Okhla': (28.543194, 77.275955), 'Jasola Apollo': (28.538084, 77.285538), 'Sarita Vihar': (28.528622, 77.288345), 'Mohan Estate': (28.51959, 77.294518), 'Tughlakabad': (28.502232, 77.29866), 'Badarpur': (28.4932, 77.30085), 'Sarai': (28.47794, 77.304932), 'NHPC Chowk': (28.462435, 77.305252), 'Mewala Maharajpur': (28.4485, 77.308098), 'Sector 28': (28.440586, 77.305992), 'Badkal Mor': (28.422707, 77.310234), 'Faridabad Old': (28.412172, 77.311272), 'Neelam Chowk Ajronda': (28.400707, 77.309105), 'Bata Chowk': (28.386362, 77.298782), 'Escorts Mujesar': (28.370199, 77.315002), 'Sikanderpur': (28.480833, 77.094246), 'PHASE 2': (28.488371, 77.092865), 'Belvedere Towers': (28.492065, 77.088142), 'Cyber City': (28.498478, 77.089088), 'Moulsari Avenue': (28.501572, 77.094536), 'PHASE 3': (28.494329, 77.093552), 'IGD Airport': (28.554869, 77.087921), 'Shivaji Stadium': (28.629007, 77.209213), 'Delhi Gate': (28.640488, 77.240303), 'Jama Masjid': (28.650393, 77.237556), 'Lal Quila': (28.657576, 77.236595), 'Okhla Bird Sanctuary': (28.552816, 77.321564), 'Kalindi Kunj': (28.542835, 77.310173), 'Jasola Vihar Shaheen Bagh': (28.546005, 77.296715), 'Okhla Vihar': (28.561255, 77.291916), 'Jamia Millia Islamia': (28.562944, 77.286209), 'Sukhdev Vihar': (28.559887, 77.275116), 'Okhla NSIC': (28.554575, 77.26487), 'Phase 1': (28.471981, 77.094009), 'Sector 42-43': (28.458475, 77.09684), 'Sector 53-54': (28.447533, 77.100487), 'Sector 54 Chowk': (28.434212, 77.104782), 'Sector 55-56': (28.424587, 77.105042), 'Majlis Park': (28.724157, 77.182068), 'Shalimar Bagh': (28.70182, 77.165184), 'Shakurpur': (28.685781, 77.149651), 'Punjabi Bagh West': (28.672747, 77.139183), 'ESI Hospital': (28.658159, 77.127319), 'Mayapuri': (28.637098, 77.129738), 'Naraina Vihar': (28.624121, 77.136482), 'Delhi Cantt': (28.608641, 77.140373), 'DD South Campus': (28.589376, 77.169518), 'Nehru Enclave': (28.545856, 77.25116), 'G.K.Enclave-I': (28.541836, 77.238243), 'Chirag Delhi': (28.541229, 77.229385), 'Panchsheel Park': (28.542339, 77.220512), 'IIT': (28.547194, 77.193832), 'R.K. Puram': (28.550486, 77.184952), 'Munirka': (28.557821, 77.174026), 'Vasant Vihar': (28.558378, 77.160774), 'Shankar Vihar': (28.560787, 77.140442), 'IGD Airport': (28.565275, 77.122391), 'Sadar Bazar': (28.577108, 77.111305), 'PALAM': (28.589067, 77.082954), 'Dashrathpuri': (28.602333, 77.08255), 'Dabri Mor': (28.615904, 77.085258), 'Mundka IA': (28.68396, 76.989822), 'Ghevra': (28.685289, 76.993584), 'Tikri Kalan': (28.686899, 76.977249), 'Tikri Border': (28.687876, 76.963783), 'Pandit Shree Ram Sharma': (28.689213, 76.951088), 'Bahadurgarh City': (28.690784, 76.935265), 'Brigadier Hoshiyar Singh': (28.697428, 76.919128), 'SV Moti Bagh': (28.578529, 77.175713), 'Bhikaji Cama Place': (28.570208, 77.187866), 'Sarojini Nagar': (28.570208, 77.187866), 'South Extension': (28.5686, 77.219818), 'Trilokpuri': (28.613506, 77.308678), 'East Vinod Nagar': (28.620052, 77.305588), 'Mandawali-West Vinod Nagar': (28.624861, 77.304146), 'IP Extension': (28.631599, 77.310898), 'Karkardooma': (28.649473, 77.295341), 'Krishna Nagar': (28.65782, 77.290306), 'East Azad Nagar': (28.665043, 77.284599), 'Jafrabad': (28.682943, 77.27507), 'Maujpur': (28.692057, 77.280922), 'Gokulpuri': (28.703009, 77.286301), 'Johri Enclave': (28.713297, 77.290154), 'Shiv Vihar': (28.721863, 77.289635), 'Sant Surdas Sihi': (28.354666, 77.316261), 'Raja Nahar Singh': (28.339899, 77.331657), 'Vinobapuri': (28.566179, 77.249367), 'Ashram': (28.576065, 77.25753), 'Hazrat Nizamuddin': (28.5889, 77.253189), 'Mayur VPKT1': (28.606598, 77.296326), 'Sector-34 Noida': (28.580229, 77.363518), 'Sector-52 Noida': (28.586849, 77.372749), 'Sector-61 Noida': (28.597677, 77.372368), 'Sector-59 Noida': (28.609089, 77.372955), 'Sector-62 Noida': (28.616991, 77.373611), 'Noida Electronic City': (28.628685, 77.375229)}

# {'Noida Sector 51': (28.585548, 77.375374), 'Noida Sector 50': (28.574547, 77.378357), 'Noida Sector 76': (28.565445, 77.37973), 'Noida Sector 101': (28.556065, 77.385056), 'Noida Sector 81': (28.549259, 77.390099), 'NSEZ': (28.532248, 77.394951), 'Noida Sector 83': (28.522284, 77.396477), 'Noida Sector 137': (28.510817, 77.403625), 'Noida Sector 142': (28.498999, 77.412567), 'Noida Sector 143': (28.494246, 77.422318), 'Noida Sector 144': (28.486376, 77.432968), 'Noida Sector 145': (28.47913, 77.442307), 'Noida Sector 146': (28.468822, 77.455101), 'Noida Sector 147': (28.4594, 77.465965), 'Noida Sector 148': (28.448021, 77.476692), 'Knowledge Park': (28.456865, 77.500298), 'Pari Chowk': (28.463331, 77.508308), 'Alpha 1': (28.470879, 77.512718), 'Delta 1': (28.478374, 77.525581), 'GNIDA Office': (28.484531, 77.536621), 'Depot Station': (28.488651, 77.544075)}

m = folium.Map(location=coordinates[list(coordinates)[0]], zoom_start= 5)

for i in coordinates:
    if i in lines.yellow_line2:
        folium.Marker(coordinates[i], popup=f"{i}", icon=folium.CustomIcon(icon_image = 'markers/yellow_ico.png', icon_size=(20,30))).add_to(m)

    if i in lines.red_line1:
        folium.Marker(coordinates[i], popup=f"{i}", icon=folium.CustomIcon(icon_image = 'markers/red_ico.png', icon_size=(40,40))).add_to(m)

    if i in lines.blue_line3 or i in lines.blue_line4:
        folium.Marker(coordinates[i], popup=f"{i}", icon=folium.CustomIcon(icon_image = 'markers/blue_ico.png', icon_size=(20,30))).add_to(m)
    
    if i in lines.green_line5:
        folium.Marker(coordinates[i], popup=f"{i}", icon=folium.CustomIcon(icon_image = 'markers/green_ico.png', icon_size=(20,30))).add_to(m)

    if i in lines.violet_line6:
        folium.Marker(coordinates[i], popup=f"{i}", icon=folium.CustomIcon(icon_image = 'markers/violet_ico.png', icon_size=(20,30))).add_to(m)

    if i in lines.pink_line7:
        folium.Marker(coordinates[i], popup=f"{i}", icon=folium.CustomIcon(icon_image = 'markers/pink_ico.png', icon_size=(20,30))).add_to(m)

    if i in lines.magenta_line8:
        folium.Marker(coordinates[i], popup=f"{i}", icon=folium.CustomIcon(icon_image = 'markers/magenta_ico.png', icon_size=(20,30))).add_to(m)

m.save("maps__.html")

#yellow
# https://www.clipartmax.com/png/full/86-869339_yellow-map-marker-png.png

#red (40, 40)
# 'https://freesvg.org/img/map-pin.png'

print(len(coordinates))