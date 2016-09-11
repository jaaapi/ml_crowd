def get_ignored_cols():
    return ['collections_12_mths_ex_med', 'dti', 'funded_amnt', 'dti_joint',
            'funded_amnt_inv', 'fico_range_high', 'fico_range_low',  'id',
            'int_rate', 'issue_d', 'last_fico_range_high', 'last_fico_range_low',
            'last_pymnt_amnt', 'last_pymnt_d', 'member_id', 'next_pymnt_d',
            'policy_code',  'total_pymnt_inv', 'total_rec_int', 'url',
            'open_acc_6m', 'open_il_6m', 'open_il_12m', 'open_il_24m', 'mths_since_rcnt_il',
            'total_bal_il', 'il_util', 'open_rv_12m', 'open_rv_24m', 'max_bal_bc', 'all_util',
            'total_rev_hi_lim', 'inq_fi', 'total_cu_tl', 'inq_last_12m', 'acc_now_delinq',
            'tot_coll_amt', 'tot_cur_bal'
            ]


def get_input_cols():
    return ['addr_state', 'annual_inc', 'application_type',
            'delinq_2yrs', 'earliest_cr_line', 'emp_length',  'funded_amnt',
            'home_ownership', 'initial_list_status', 'inq_last_6mths', 'installment',
            'last_credit_pull_d', 'loan_amnt', 'mths_since_last_delinq',
            'mths_since_last_major_derog', 'mths_since_last_record', 'open_acc',
            'pub_rec', 'purpose', 'term', 'total_acc', 'zip_code'
            ]


def get_text_cols():
    return ['desc', 'emp_title', 'title']


def get_output_col():
    return {'name': 'loan_status', 'type': 'string', 'values': ['Charged Off', 'Fully Paid']}


def get_output_cols():
    return ['collection_recovery_fee', 'int_rate', 'loan_status', 'out_prncp',
            'out_prncp_inv', 'pymnt_plan', 'recoveries', 'revol_bal', 'revol_util',
            'sub_grade', 'grade', 'total_pymnt', 'total_rec_late_fee', 'total_rec_prncp'
           ]


def get_output_mapping():
    return {'Charged Off': 1, 'Fully Paid': 0}















