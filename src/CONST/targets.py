class Targets:
    ab_classes: dict[str, list[str]] = {
        "beta_lactams": [ # beta-lactams
                "amoxicillin", # penicillins
                "piperacillin",
                "ticarcillin",
                "cefepime", # cephalosporins
                "cefazolin",
                "ceftolozane",
                "ceftriaxone",
                "ceftazidime",
                "aztreonam", # monobactam
                "imipenem", # carbapenems
                "meropenem",
                "doripenem"
            ],
        "glycopeptide": ["vancomycin"],
        "tetracyclines": [
                "minocycline",
                "tigecycline",
                "doxycycline",
                "tetracycline",
                "chlortetracycline"
            ],
        "macrolides": [
                "azithromycin", # macrolides
                "erythromycin",
                "clarithromycin"
            ],
        "chlorampennicol": [
                "chlorampenicol"
            ],
        "oxazolidinones": [
                "linezolid"
            ],
        "rifampicin": [
                "rifampicin"
            ],
        "phosphonic": [
                "fosfomycin"
            ],
        "aminoglycosides": [
                "amikacin", # aminoglycosides
                "tobramycin",
                "streptomycin",
                "kanamycin"

            ],
        "trimethoprim": [
                "trimethoprim" # trimethoprim
            ],
        "sulfonamide": [
                "sulfamethoxazole" # sulfamethoxazole
            ],
        "quinolones": [
                "ciprofloxacin", # quinolones
                "levofloxacin",
                "moxifloxacin"
            ]
    }

    TARGETS: dict[str, list[str]] = {
            "6I1H": ab_classes["beta_lactams"],
            "1FVM": ab_classes["glycopeptide"],
            "8CF1": ab_classes["tetracyclines"],
            "8CGD": (
                    ab_classes["macrolides"] +
                    ab_classes["chlorampennicol"]
                ),
            "1NJ1": (
                    ab_classes["macrolides"] +
                    ab_classes["chlorampennicol"]
                ),
            "7S1H": ab_classes["oxazolidinones"],
            "1YNN": ab_classes["rifampicin"],
            "1YBG": ab_classes["phosphonic"],
            "4DUH": ab_classes["quinolones"],
            "8C41": ab_classes["quinolones"],
            "1FJG": ab_classes["aminoglycosides"],
            "3FL9": ab_classes["trimethoprim"],
            "1TX2": ab_classes["sulfonamide"],
            "3TZF": ab_classes["sulfonamide"]
        }

    AMR_TAR: dict[str, list[str]] = {
            "5M18": ab_classes["beta_lactams"],
        }
