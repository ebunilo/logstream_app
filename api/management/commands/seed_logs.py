from django.core.management.base import BaseCommand
from api.models import LogEntry

import random
import time

class Command(BaseCommand):
    help = 'Seed the database with sample log entries'

    def handle(self, *args, **kwargs):
        TOTAL_LOGS = 5_000_000
        BATCH_SIZE = 10_000
        LEVELS = ['INFO', 'WARNING', 'ERROR', 'DEBUG', 'CRITICAL']
        SERVICES = ['auth-service', 'payment-service', 'user-service', 'notification-service', 'analytics-service']
        
        self.stdout.write(self.style.SUCCESS(f'Starting to seed {TOTAL_LOGS} log entries in batches of {BATCH_SIZE} ...')
        )
        start_time = time.time()
        
        batch = []
        for i in range(TOTAL_LOGS):
            log_entry = LogEntry(
                service_name=random.choice(SERVICES),
                level=random.choice(LEVELS),
                message=f'Sample log message {i+1}'
            )
            batch.append(log_entry)
            
            if len(batch) >= BATCH_SIZE:
                LogEntry.objects.bulk_create(batch)
                batch = []
                self.stdout.write(f'Seeded {i + 1} / {TOTAL_LOGS} log entries...')
        
        # Create any remaining log entries that didn't fill a complete batch
        if batch:
            LogEntry.objects.bulk_create(batch)
        
        end_time = time.time()
        self.stdout.write(self.style.SUCCESS(f'Finished seeding {TOTAL_LOGS} log entries in {end_time - start_time:.2f} seconds.'))
        