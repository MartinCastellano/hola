

char*
fizzbuzz (int n){
    

    int     i, digits;
    char    *tmp;

    if (n % 15 ==0) {

        return (strdup("fizzbuzz")) ;

    }else if (n % 5 == 0) {

        return (strdup ("buzz")) ;

    }else if (n % 3 == 0){

        return (strdup ("fizz"));
    }
    
    for (digits= 0, i= n; i != 0; digits++ , i /= 10);

    tmp = malloc((digits+ 1) * sizeof(char));
    
    // if (tmp == NULL ){
    //     return NULL;
    // }

    snprintf(tmp, digits + 1, "%d", n);

    return(tmp);

}

