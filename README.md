# SpiderDAAD
Welcome to my open source !
=======================

It's a test spider for catch the inf from DAAD 

I found that the web site of orgnization DAAD use Taffydb to save the informations of PHD offers, so i find the way that can get all informations like Json

```javascript
............
       jtaffy = response.body.replace('var offers = TAFFY(', '').replace(');', '')

       with open('data2.json', 'w') as fout:
           fout.write(jtaffy)
       fout.close()

       with open('data2.json', 'r') as fin:
           # data = f.readlines()
           data = json.load(fin)
       fin.close
       # count = linecache.getlines('data2.json')
       # linecache.clearcache()
       # data = json.load('data2.json')
       .............................
```
But the reason why after deleting the head and the end of Taffydb, i can't take all data as same as Json. Need to find the ansower.
