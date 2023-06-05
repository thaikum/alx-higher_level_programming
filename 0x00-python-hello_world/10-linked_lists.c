#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n; /* number of nodes */

	current = h;
	n = 0;
	while (current != NULL)
	{
		printf("%i\n", current->n);
		current = current->next;
		n++;
	}

	return (n);
}

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;

	return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}

int check_exists(listint_t *list, listint_t *test)
{
	listint_t *head;

	if (head = list; head; head = head->next)
		if (head == test)
			return (1);
	return (0);
}

/**
 * check_cycle - checks if a linked link contains a cycle
 * @list: the list to check the cycle
 *
 * Return: 1 if there is a cycle 0 ir not
 */
int check_cycle(listint_t *list)
{
	int x;
	listint_t *head = list, *hist_head = NULL;

	items[0] = NULL;

	if (!head || !items)
	{
		return (0);
	}
	else
	{
		for (; head; head = head->next)
		{
			if (head->next)
			{
				if (check_cycle(hist_head, head->next))
				{
					free_listint(list);
					free_listint(hist_head);
					return (1);
				}
				hist_head = add_nodeint(hist_head, head->n)
				return ();
			}
			else
				return (0);
		}
	}
}
