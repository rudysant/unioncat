Catalogue record sharing and exchange

Post : save catalogue record
Get : read catalogue record
Put : update catalogue record
Delete : remove catalogue record

Model (book) :
- id
- title
- author (foreignkey from authority record)
- place of publication
- publisher name
- date of publication
- physical data : number of pages
- owner (foreignkey from holder record)

Model (author)
- id
- name

Model (publisher)
- id
- name
- address

Model (holder)
- id
- name
- address
