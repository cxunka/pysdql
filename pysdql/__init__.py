from pysdql.core.api import (
    Relation,
    ConcatExpr
)
from pysdql.const import (
    PART_COLS,
    SUPPLIER_COLS,
    PARTSUPP_COLS,
    CUSTOMER_COLS,
    ORDERS_COLS,
    LINEITEM_COLS,
    NATION_COLS,
    REGION_COLS
)


def merge(*args, on=None, optimize=False):
    ie_list = []
    ik_list = []
    iv_list = []
    for r in args:
        ie_list.append(str(r.iter_expr))
        ik_list.append(str(r.iter_expr.key))
        iv_list.append(str(r.iter_expr.val))

    iv_str = " * ".join(iv_list)

    ie_str = ' '.join(ie_list)

    con_str = f'if({on})\n  {{ {concat(ik_list)} -> {iv_str} }}'

    print(f'let R = {ie_str} {con_str} in')

    return Relation('R')


def concat(keys: list) -> str:
    keys.reverse()
    k1 = keys.pop()
    k2 = keys.pop()
    ce = ConcatExpr(rec1=k1, rec2=k2)
    keys.reverse()
    for k in keys:
        ce = ce.concat(k)
    return str(ce)