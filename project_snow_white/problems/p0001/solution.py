INPUT = 'v1emyc6nl0b5f7ieqlr4lssi5ezj3xif57ur06emavbomvd0etjbr2nnop09x57ie68alsnkljcxg0rru67wq3fo6si7l1k1t7h3t4uvtemwl31vfhmbfx35vy4468wr7l4uwhaz0jibz2hyeuv3u17e1d5xars4y3qu2f5c2fbxgj6hmij11830dkpd2hq69uod80m1hrl23m3ewahccekszd3qvdvwg40peqreke1rzefce967jwza4wv01irjt9qkltlh4igil4d7ko97zrbgtg4ulp3sfm55xyov3mkfzfh0084yyjq51zof8v8cfha09tr5h116hcrahwwng4bx0nnj4lgd2l1ehvc8yl2xgs3vvqdhxwe608vp723elroynrmzw1kb5ku6q3glp26ipok80ud8755elpnrq1sribwxfwcia18vpa9bkv86u27cen212v56x5z2p45c415nixibeg8s1yy12h1vh5zwyj5obxgang25f515u5hxtqbc4nkkhddmaiyzurcnghyen9ppvu0eatsg55em1a5pl7rc3fdgxqrb6qbk458seo08zuyq863yelfsy27d8rvlecy4j0uqhsby0bppr0lgt7t4fqz4jmluhf2gvucgufkmka37t0vodlmkdhod9anqkikmoysnydkr3k8mnwcir3btlkge7qhh1omlslmskui684fzt2hzcuppqw3a58a0cl30m6s18sf15gtcb8njvojgply38jwi9owsyrs2l6rq86nqlmcw499fhxe1jr37zzebqe54nhsnk6ewoz6hb8bf1lengmz6zagvk5ltrwqnep0kb04f01j10bvc77ffvsnxt479gwqzjhehq1m7vay8el3xf7b8gsoebhc3pds8yttzbqzebe970wr4nnfkxx216q26vvwsi22u6vzf5i0i5gx3cmihss92yhxnvfozx8vje0yxursrcmj01abhjprxhtw44c1irrfv'


def add_numbers_in_alphanumeric_string(alphanumeric_string: str) -> int:
    numbers_sum = 0
    power = 0
    for c in reversed(alphanumeric_string):
        if c.isdigit():
            if c != '0':
                numbers_sum += int(c) * 10 ** power
            power += 1
        else:
            power = 0
    return numbers_sum


if __name__ == '__main__':
    print(add_numbers_in_alphanumeric_string(INPUT))
