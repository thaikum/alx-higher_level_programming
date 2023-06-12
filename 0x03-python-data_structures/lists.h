#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/**
 * struct double_list - doubly linked list
 * @prev: pointer to previous node
 * @n: the value
 * @next: pointer to next node
 *
 * Description: doubly linked list to handle the palindrome
 */
typedef struct double_list
{
	struct double_list *prev;
	int n;
	struct double_list *next;
} double_s;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

#endif /* LISTS_H */
