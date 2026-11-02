import csv, math, sys, collections as C
rows=list(csv.DictReader(open(sys.argv[1],encoding='utf-8-sig')))
print('matches',len({r['match_id'] for r in rows}),'rows',len(rows))
o=[r for r in rows if r['excluded_set_piece_restart']=='False']
for p in '01':
    s=[r for r in o if r['under_pressure']==p]
    c=C.Counter(r['pass_direction'] for r in s)
    ev=[r for r in s if r['included_in_success_rate']=='True']
    fw=[r for r in ev if r['pass_direction']=='전진']
    print(p,len(s),{k:round(v/len(s)*100,2) for k,v in c.items()},
      'succ',round(sum(int(r['pass_success']) for r in ev)/len(ev)*100,2),
      'fwd succ',round(sum(int(r['pass_success']) for r in fw)/len(fw)*100,2))
for k in ['전진','횡','후방']:
    a=[abs(math.degrees(float(r['pass_angle']))) for r in o if r['pass_direction']==k]
    print(k,round(min(a),1),round(max(a),1))
print('x',min(float(r['start_x']) for r in o),max(float(r['end_x']) for r in o))
print('y',min(float(r['start_y']) for r in o),max(float(r['end_y']) for r in o))
