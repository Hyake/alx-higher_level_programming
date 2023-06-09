#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: points to a struct of type listint_t
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slw = list;
	listint_t *fast = list;

	if (!list)
		return (0);
	while (fast && fast->next)
	{
		slw = slw->next;
		fast = fast->next->next;
		if (fast == slw)
			return (1);
	}
	return (0);
}
