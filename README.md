# Kieser-App-flet
Trainings companion for Kieser Training

## Motivation
Using Flet, instead of pure Flutter/Dart.

# Folder structure
## assets/fonts
There are three font files located:
| Font | Purpose |
|------|---------|
| Raleway | Default font, currently in use via Theming |
| OpenSans | Backup font, as alternative to "Raleway", not in use yet. |
| KieserApp | font being used make user interface nicer. It has been created to provide custom icons into play, like a "Dumpbell".

## assets/datasets
It is similar to a R/O database maintained by "model classes" (see below).
| File | Purpose |
|------|---------|
| Customer.json | List of Kieser customers (only one at the moment ;-) |
| Machines.json | All machines available in Kieseer studios with all their descriptive data, and parameters for setup of the machine before exercise starts. |
| Plans.json | Defines the machines assigned to customer including the settings for each machine's parameters and datails about movement defined by Kieser instructor.<br/>


