#include "lists.h"
/**
 * check_exists - checks if a node exists in a linked list
 * @list: the list head
 * @test: te node to check
 * @terminal: where to stop looping
 *
 * Return: 1 if found or 0 if not
 */
int check_exists(listint_t *list, listint_t *test, listint_t *terminal)
{
	listint_t *head;

	for (head = list; head && head != terminal; head = head->next)
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
	listint_t *head = list;

	if (!head)
	{
		return (0);
	}
	else
	{
		for (; head; head = head->next)
		{
			if (head->next)
			{
				if (head->next->n == 0x1000000)
					return (1);

				head->next->n = 0x1000000;
			}
			else
				return (0);
		}
	}
	return (0);
}
