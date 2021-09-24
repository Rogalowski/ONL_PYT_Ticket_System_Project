# ONL_PYT_Ticket_System_Project
Ticketing System Project


TICKETING SYSTEM
System do zarządzania zgłoszeniami tt (trouble ticket) dotyczącymi problemami technicznymi użytkowników.
Narazie jako admin może kazdy tt wystwaic do kazdego
Główna strona:
- panel logowania
- inforamcja firmy i ze to system ticketowy
- statystyki o  ilości tt na kazdym z działów (po kliknieciu na dzial przechodzi do kolejki tt) (jeśli ma uprawnienia)
- Szczegoly zalogowanego uzytkownika

Panel zalogowanego uzytkownika :
- widoczne inforamcje o uztkowniku (mozliwosc zmiany hasla)
- widoczne statystyki – ogolna ilosc rozwiazanych tt
- widoczne tickety przypisane na dana osobe
- widoczne tt przypisane ogolne do dzialu
- widoczny link do wszystkich tt danego działu (nie rozpoatruje confidetiali)

Zawartość tt:
- Id tt
- Tytuł
- Opis
- Status
- priorytet (Low, Medium, High, ASAP) 
- data utworzenia
- data zakonczenia ( po dodaniu  statusu resolved, doda tez komentarz)
- Korespondencja dla pracowników  z data wystawienia, przez kogo
- Dział do którego jest wystawiony tt
- Kategoria Problemu
- Przypisanie
- kto wystawił tt i z jakiego działu
- mozliwosc dodania plików/zdjęć (opcjonalne)
- historia zmian ticketa (opcjonalnie)

Statusy tt:
- Not Acknowledged
- Pending (schedule, requestor information,  
- Work in Progress
- Resolved (Successfull, not successfull, 

Działy (listy kolejek- po wybraniu na głownej stronie przejscie do logowania): 
- IT (Information Technology),
- HR (Human Resources),
- PM (Project Management),
- F&B (Finance & Buyers)
IT

Dział IT Kategorie problemów: Desktops/laptops, Pherieral devices, Mobile Devices, Network Infrastructure 

Typy problemu dla  Desktops/laptops: 
- Operating System 
- Application
- Hardware
- Other

Typy problemu dla Pherieral devices:
- no conection
- need assistance
- broken
- other

Typy problemu dla Mobile devices:
- no connection
- no respond
- broken device/battery
- other

Typy problemu dla Infrastructure devices:
- network/connection
- maintenance
- upgrade/update
- other

HR 
Dział HR Kategorie problemów: Work Schedule, Hiring Process, Umowa, Documents
Typy problemu dla  Work Schedule: overtime/delegation, work time issue, change work time, other

PM
Dział PM Kategorie problemów: Project realization, Improvement, Inspection
 
F&B
Dział PM Kategorie problemów: Invoices, Payment, Delegation payment, contracts