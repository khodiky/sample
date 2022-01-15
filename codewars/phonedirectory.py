## https://www.codewars.com/kata/56baeae7022c16dd7400086e

def phone(strng, num):
    cnt = strng.count(num)
    if cnt == 0:
        return "Error => Not found: " + num
    elif cnt > 1:
        return "Error => Too many people: " + num

    contacts = strng.split("\n")
    for contact in contacts:
        if num in contact:
            name = contact[contact.index("<")+1:contact.index(">")]
            contact = contact.replace(num, "").replace(name, "")
            for c in "/:!<>+;_$*?,":
                contact = contact.replace(c, " ")
            address = " ".join(contact.split())
    return "Phone => {}, Name => {}, Address => {}".format(num, name, address)
