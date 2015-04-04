import json
from pprint import pprint
from operator import itemgetter
json_data=open('val.json').read()
loc = {}
#loc.setdefault = "NOT FOUND"
data = json.loads(json_data)
#pprint(data)

def arrange_everything(data):
	#data = sorted(data,key=lambda k: k.get('advertiser_id',0),reverse=False)
	#data = sorted(data,key=lambda k: k.get('advertiser_id','ymd'),reverse=False)
	#data = sorted(data,key=lambda k: k.get('advertiser_id'),reverse=False)
	data = sorted(data,key=itemgetter('advertiser_id','ymd'))
	#for i to xrange(data)
	loc[data[0]['advertiser_id']] = 0
	for i in range(1,len(data)):
		if(data[i]['advertiser_id'] != data[i-1]['advertiser_id']):
			loc[data[i]['advertiser_id']] = i
			#print data[i]['advertiser_id']	
	#pprint(data);
	return data;
	#for i in xrange(1,data):
	#	print i;
		#if(data[i-1]['ymd'] < data[1]['ymd'])
		


def counting(input):
	#print "1"
	for x in input:
		try:
			temp = loc[x]
		except KeyError:
			print "%r doesn't exist " % x
			continue
		success = None
		print "\n"
		print 'Advertise ID : %r' % x
		cumulative_click = 0
		cumulative_impression = 0
		while(not(success)):
			print 'Date : %r ' % data[temp]['ymd']
			cumulative_click += data[temp]['num_clicks']
			cumulative_impression += data[temp]['num_impressions']
			print 'Cumulative Click : % r ' % cumulative_click
			print 'Cumulative Impression : % r ' % cumulative_impression
			if(len(data)-1 == temp):
				success = 1
			else:
				#print len(data)
				if(data[temp]['advertiser_id']!= data[temp+1]['advertiser_id']):
					success = 1;
			temp = temp+1

			
	#for i in xrange(data)
	
	#data['aggregate'] = '0'
	#pprint(data)	

data = arrange_everything(data)
#pprint(data);
#print data[1][advertiser_id]
counting([400,200,222])
#print loc;
