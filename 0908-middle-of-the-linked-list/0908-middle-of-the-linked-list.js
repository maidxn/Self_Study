/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
    let count = 0;
    let temp = head;
    while (temp != null){
        count += 1;
        temp = temp.next;
    }
    const index = count % 2 == 0 ? (count / 2)  : Math.floor(count / 2);
    let count_index = 0;
    let res = head;
    while(count_index < index){
        count_index += 1;
        res = res.next;
    }
    return res;
};