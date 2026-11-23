	import tkinter as tk
	from tkinter import messagebox
	# Farben
	BG = "#1e1e2e"
	CARD = "#313244"
	BLUE = "#89b4fa"
	GREEN = "#a6e3a1"
	RED = "#f38ba8"
	punkte = 0
	max_punkte = 0
	szenarien = {
	    "Homeoffice für neue Mitarbeiterin": {
	        "lernfelder": "LF1, LF2, LF3, LF4",
	        "schritte": [
	            {
	                "frage": "Welche Hardware wird bereitgestellt?",
	                "optionen": {
	                    "A) Firmenlaptop mit Dockingstation": (True, "Richtig! Weiter zur nächsten Entscheidung."),
	                    "B) Privater Laptop der Mitarbeiterin": (False, "Sicherheitsrichtlinien werden verletzt."),
	                    "C) Alter Firmen-PC ohne Prüfung": (False, "Leistungs- und Sicherheitsprobleme möglich.")
	                }
	            },
	            {
	                "frage": "Wie wird der Netzwerkzugang eingerichtet?",
	                "optionen": {
	                    "A) VPN-Zugang konfigurieren": (True, "Richtig! Weiter zur nächsten Entscheidung."),
	                    "B) Zugriff ohne VPN erlauben": (False, "Datenschutzrisiko."),
	                    "C) Mitarbeiterin soll selbst konfigurieren": (False, "Fehleranfällige Einrichtung.")
	                }
	            },
	            {
	                "frage": "Wie wird der Schutzbedarf berücksichtigt?",
	                "optionen": {
	                    "A) Schutzbedarf analysieren und Sicherheitsmaßnahmen festlegen": (True, "Homeoffice erfolgreich eingerichtet!"),
	                    "B) Keine Analyse durchführen": (False, "Sicherheitslücken bleiben unentdeckt."),
	                    "C) Nur Passwortschutz aktivieren": (False, "Schutzmaßnahmen nicht ausreichend.")
	                }
	            }
	        ]
	    },
	    "Neuer Arbeitsplatz im Büro": {
	        "lernfelder": "LF1, LF2, LF4",
	        "schritte": [
	            {
	                "frage": "Ein Mitarbeiter benötigt einen neuen Arbeitsplatz für CAD-Anwendungen.",
	                "optionen": {
	                    "A) Anforderungen analysieren": (True, "Richtig!"),
	                    "B) Billigsten Rechner bestellen": (False, "Leistung reicht vermutlich nicht aus."),
	                    "C) Alten Rechner weiterverwenden": (False, "Zu geringe Leistung.")
	                }
	            },
	            {
	                "frage": "Welche Software wird beschafft?",
	                "optionen": {
	                    "A) Lizenzierte Software bestellen": (True, "Richtig!"),
	                    "B) Kostenlose Software aus unbekannter Quelle": (False, "Sicherheitsrisiko."),
	                    "C) Gecrackte Software verwenden": (False, "Rechtswidrig.")
	                }
	            },
	            {
	                "frage": "Wie wird der Arbeitsplatz eingerichtet?",
	                "optionen": {
	                    "A) Ergonomie berücksichtigen": (True, "Arbeitsplatz erfolgreich eingerichtet!"),
	                    "B) Bildschirm beliebig aufstellen": (False, "Ergonomische Probleme."),
	                    "C) Ohne Sicherheitsprüfung freigeben": (False, "Sicherheitsrisiko.")
	                }
	            }
	        ]
	    },
	    "Neuer Client im Firmennetzwerk": {
	        "lernfelder": "LF2, LF3, LF4",
	        "schritte": [
	            {
	                "frage": "Wie wird die IP-Adresse vergeben?",
	                "optionen": {
	                    "A) Feste IP gemäß Netzwerkplan": (True, "Richtig!"),
	                    "B) Zufällige IP-Adresse": (False, "IP-Konflikte möglich."),
	                    "C) Keine IP-Konfiguration": (False, "Keine Netzwerkverbindung.")
	                }
	            },
	            {
	                "frage": "Der PC hat keinen Internetzugang. Was wird geprüft?",
	                "optionen": {
	                    "A) Gateway und DNS prüfen": (True, "Richtig!"),
	                    "B) Rechner neu kaufen": (False, "Nicht zielführend."),
	                    "C) Problem ignorieren": (False, "Netzwerkproblem bleibt bestehen.")
	                }
	            },
	            {
	                "frage": "Wie wird der Rechner abgesichert?",
	                "optionen": {
	                    "A) Virenschutz und Updates installieren": (True, "Client erfolgreich eingebunden!"),
	                    "B) Firewall deaktivieren": (False, "Großes Sicherheitsrisiko."),
	                    "C) Schutz später durchführen": (False, "System bleibt angreifbar.")
	                }
	            }
	        ]
	    }
	}
	aktuelles_szenario = None
	aktueller_schritt = 0
	
	def starte_szenario(name):
	    global aktuelles_szenario
	    global aktueller_schritt
	    aktuelles_szenario = name
	    aktueller_schritt = 0
	    lernfelder.config(
	        text="Verknüpfte Lernfelder: " +
	        szenarien[name]["lernfelder"]
	    )
	    lade_schritt()
	
	def lade_schritt():
	    schritt = szenarien[aktuelles_szenario]["schritte"][aktueller_schritt]
	    frage_label.config(
	        text=schritt["frage"]
	    )
	    for widget in button_frame.winfo_children():
	        widget.destroy()
	    for text, daten in schritt["optionen"].items():
	        btn = tk.Button(
	            button_frame,
	            text=text,
	            width=60,
	            height=2,
	            font=("Segoe UI", 11, "bold"),
	            bg=CARD,
	            fg="white",
	            activebackground=BLUE,
	            activeforeground="black",
	            relief="flat",
	            command=lambda d=daten: pruefe_antwort(d)
	        )
	        btn.pack(pady=8)
	
	def pruefe_antwort(daten):
	    global aktueller_schritt
	    global punkte
	    global max_punkte
	    richtig, meldung = daten
	    max_punkte += 1
	    if richtig:
	        punkte += 1
	        punkte_label.config(
	            text=f"⭐ Punkte: {punkte}"
	        )
	        if aktueller_schritt < len(
	                szenarien[aktuelles_szenario]["schritte"]) - 1:
	            messagebox.showinfo(
	                "✅ Richtig",
	                meldung
	            )
	            aktueller_schritt += 1
	            lade_schritt()
	        else:
	            prozent = (punkte / max_punkte) * 100
	            if prozent >= 90:
	                note = 1
	            elif prozent >= 80:
	                note = 2
	            elif prozent >= 67:
	                note = 3
	            elif prozent >= 50:
	                note = 4
	            else:
	                note = 5
	            messagebox.showinfo(
	                "🎉 Prüfung abgeschlossen",
	                f"""Szenario erfolgreich abgeschlossen!
	Punkte: {punkte}/{max_punkte}
	Note: {note}
	✅ Bestanden
	"""
	            )
	    else:
	        messagebox.showerror(
	            "❌ Falsche Entscheidung",
	            meldung
	        )
	
	root = tk.Tk()
	root.title("IT-Prüfungssimulator LF1-4")
	root.geometry("1000x700")
	root.configure(bg=BG)
	titel = tk.Label(
	    root,
	    text="🎓 IT-Prüfungssimulator LF1-4",
	    font=("Segoe UI", 24, "bold"),
	    bg=BG,
	    fg="white"
	)
	titel.pack(pady=20)
	subtitle = tk.Label(
	    root,
	    text="Praxisnahe IT-Entscheidungen und Prüfungsvorbereitung",
	    font=("Segoe UI", 11),
	    bg=BG,
	    fg="#cccccc"
	)
	subtitle.pack()
	punkte_label = tk.Label(
	    root,
	    text="⭐ Punkte: 0",
	    font=("Segoe UI", 12, "bold"),
	    bg=BG,
	    fg=GREEN
	)
	punkte_label.pack(pady=10)
	tk.Label(
	    root,
	    text="Wähle ein Szenario:",
	    font=("Segoe UI", 14, "bold"),
	    bg=BG,
	    fg="white"
	).pack(pady=10)
	dashboard = tk.Frame(root, bg=BG)
	dashboard.pack()
	for name in szenarien.keys():
	    btn = tk.Button(
	        dashboard,
	        text=name,
	        width=45,
	        height=2,
	        bg=BLUE,
	        fg="black",
	        font=("Segoe UI", 11, "bold"),
	        relief="flat",
	        command=lambda n=name: starte_szenario(n)
	    )
	    btn.pack(pady=8)
	lernfelder = tk.Label(
	    root,
	    text="",
	    font=("Segoe UI", 11, "italic"),
	    bg=BG,
	    fg="#cccccc"
	)
	lernfelder.pack(pady=15)
	frage_label = tk.Label(
	    root,
	    text="Wähle oben ein Szenario aus.",
	    wraplength=800,
	    font=("Segoe UI", 16, "bold"),
	    bg=BG,
	    fg="white"
	)
	frage_label.pack(pady=20)
	button_frame = tk.Frame(root, bg=BG)
	button_frame.pack()
root.mainloop()
