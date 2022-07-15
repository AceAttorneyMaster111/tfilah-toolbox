# Service Generator
## Landing Page
- Services arranged as clickable blocks inline.
- Each service is a `div`. Within the `div` are the title, a short description, a link to more info, and a link to start.
## Creating a Service
- Progress bar?
- How should we store it as we go?
  - It has to be encoded into the url right? Maybe as JSON? I feel like it would be better stored as XML, but not sure how to encode that into URL.
  - Or we can write a file and update it as we go? Doesn't seem very storage efficient.
  - Maybe we store it as a cookie? That way, it's saved as we go? Seems complicated.
- Start with metadata: title, mood, theme, location, time, space, etc.
  - User can make their own metadata fields?
  - Also style things.
  - Use JavaScript to show style preview? Lorem ipsum style
- Each page, use a `select` to determine what the next thing is: next prayer (say what it is), reading, iyun, etc.
  - How to account for out-of-place prayers?
- Option to skip prayer
- Save and quit, resume later
- After final prayer, instead of next prayer, the option is to "finalize". That's a new view.
  - Displays complete cue sheet.
  - Option to download service as XML or whatever
  - Option to download cue sheet PDF
  - Option to download chord packet PDF
  - Able to edit individual pieces
- Maybe no need to force people to make it start to finish?
## Other
- Upload and edit already created services. Should be able to jump in and out of any part of the process.
