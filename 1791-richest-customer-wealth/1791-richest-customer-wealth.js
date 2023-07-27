/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    let max_sum = 0;
    for (let i = 0; i < accounts.length; i++){
        let temp_sum = 0;
        accounts[i].forEach(money => {
            temp_sum += money;
        })
        max_sum = temp_sum >= max_sum ? temp_sum : max_sum;
    };
    return max_sum;
};