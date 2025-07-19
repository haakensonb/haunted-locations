# db models

## haunted_location:
- id
- title (text)
- location (fk to location)
- description (text)
- location_type (one to one, fk to types table)
- comments (one to many, one location has many comments)
- tags (one to many, fk to tags table)
- spookiness_rating (one to many, one location has many ratings)
- photos (naive blob)
- created_by (fk, user)
- created_at (datetime)
---
Nice to have:

- last_edited_at (time)
- photos (cdn)

## location
- id
- haunted_location (fk)
- lat (float)
- long (float)
---
Nice to have, need to build out other table(s):

- country
- region
- state

## rating
- id
- submitted_by (fk, user)
- value (1-5)
- haunted_location (fk)

## location_type (house, woods, etc)
- id
- type_name (text)

## tags
- id
- tag_name (text)

## user (tbd)
- id
- username
- pass
- email

## parent_comment
- id
- haunted_location (fk)
- created_by (user, fk)
- created_at (datetime)
- description (text)

## reply_comment
- id
- parent_comment (fk)
- created_by (user, fk)
- created_at (datetime)
- description (text)
