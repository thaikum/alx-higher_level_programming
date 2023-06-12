#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>
#include "lists.h"

double_s *add_double_node(int n, double_s *tail)
{
	double_s *new_tail = malloc(sizeof(double_s));

	if (!new_tail)
		exit(98);
	new_tail->n = n;
	new_tail->prev = tail;

	if (tail)
		tail->next = new_tail;
	return (new_tail);
}

/**
 * check_palindrome - checks whether a double list is a palindrome
 * @head: the list head
 * @tail: the list tail
 *
 * @Return: 1 if is palindrome or 0 if not
 */
int check_palindrome(double_s *head, double_s *tail)
{
	double_s *h = head, *t = tail;

	if (!t || !h)
		return (0);
	if (h == t)
		return (1);
	if (h->next == t->prev)
		return (1);
	if (t->prev == NULL || h->next == NULL)
		return (0);
	if (t->n == h->n)
		return (check_palindrome(h->next, t->prev));

	return (0);
}


/**
 * is_palindrome - checks if a given linked list is a plaindrome
 * @head: the list to check
 *
 * @Return: 1 if list is palindrome and 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *cur_head = *head;
	double_s *new_head, *new_tail;

	if (!(*head) || (*head)->next == NULL)
		return (1);
	new_tail = new_head = add_double_node((*head)->n, NULL);
	cur_head = cur_head->next;
	for(;cur_head; cur_head = cur_head->next)
		new_tail = add_double_node(cur_head->n, new_tail);

	return (check_palindrome(new_head, new_tail));
}
