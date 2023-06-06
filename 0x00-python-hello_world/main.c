#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_m - singly linked list
 * @number: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_m
{
	int number;
	struct listint_m *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int number);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
