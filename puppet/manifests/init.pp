Exec {
    logoutput => on_failure,
}

import "a10n"

node default {
    include webapp::a10n
}
