from enemy import Enemy, Troll, Vampyre

ugly_troll = Troll("Pug")
print(f"Ugly troll - {ugly_troll}")

another_troll = Troll("Ug")
print(f"Another troll - {another_troll}")
another_troll.take_damage(18)
print(another_troll)

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

vlad = Vampyre("Vlad")
print(vlad)
vlad.take_damage(5)
print(vlad)

print("-" * 40)
another_troll.take_damage(30)
print(another_troll)

while vlad.alive:
    vlad.take_damage(1)
    print(vlad)
