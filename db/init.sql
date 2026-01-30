DROP TABLE IF EXISTS vm_costs;

CREATE TABLE vm_costs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    provider TEXT,
    instance_type TEXT,
    vcpu INTEGER,
    memory_gb REAL,
    price_per_hour REAL,
    region TEXT
);
