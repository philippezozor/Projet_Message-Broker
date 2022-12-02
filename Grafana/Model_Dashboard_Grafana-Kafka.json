{
    "annotations": {
      "list": [
        {
          "$$hashKey": "object:87",
          "builtIn": 1,
          "datasource": "-- Grafana --",
          "enable": true,
          "hide": true,
          "iconColor": "rgba(0, 211, 255, 1)",
          "name": "Annotations & Alerts",
          "target": {
            "limit": 100,
            "matchAny": false,
            "tags": [],
            "type": "dashboard"
          },
          "type": "dashboard"
        }
      ]
    },
    "description": "Dashboard for metrics jmx_exporter protmetheus",
    "editable": true,
    "fiscalYearStartMonth": 0,
    "gnetId": 11962,
    "graphTooltip": 0,
    "id": 8,
    "iteration": 1669992512369,
    "links": [],
    "liveNow": false,
    "panels": [
      {
        "collapsed": false,
        "datasource": {
          "type": "prometheus",
          "uid": "OYKLxrO4k"
        },
        "gridPos": {
          "h": 1,
          "w": 24,
          "x": 0,
          "y": 0
        },
        "id": 231,
        "panels": [],
        "title": "Cluster health",
        "type": "row"
      },
      {
        "description": "",
        "fieldConfig": {
          "defaults": {
            "color": {
              "mode": "thresholds"
            },
            "mappings": [
              {
                "options": {
                  "match": "null",
                  "result": {
                    "text": "N/A"
                  }
                },
                "type": "special"
              }
            ],
            "thresholds": {
              "mode": "absolute",
              "steps": [
                {
                  "color": "#d44a3a",
                  "value": null
                },
                {
                  "color": "rgba(237, 129, 40, 0.89)",
                  "value": 2
                },
                {
                  "color": "#299c46",
                  "value": 3
                }
              ]
            },
            "unit": "none"
          },
          "overrides": []
        },
        "gridPos": {
          "h": 4,
          "w": 4,
          "x": 0,
          "y": 1
        },
        "id": 647,
        "links": [],
        "maxDataPoints": 100,
        "options": {
          "colorMode": "value",
          "graphMode": "area",
          "justifyMode": "auto",
          "orientation": "horizontal",
          "reduceOptions": {
            "calcs": [
              "lastNotNull"
            ],
            "fields": "",
            "values": false
          },
          "textMode": "auto"
        },
        "pluginVersion": "8.4.5",
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "sum(kafka_server_replica_manager_leadercount{job=\"kafka\"})",
            "format": "time_series",
            "instant": false,
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "",
            "refId": "A"
          }
        ],
        "title": "Brokers Online",
        "type": "stat"
      },
      {
        "description": "",
        "fieldConfig": {
          "defaults": {
            "color": {
              "mode": "thresholds"
            },
            "mappings": [
              {
                "options": {
                  "match": "null",
                  "result": {
                    "text": "N/A"
                  }
                },
                "type": "special"
              }
            ],
            "thresholds": {
              "mode": "absolute",
              "steps": [
                {
                  "color": "#C4162A",
                  "value": null
                },
                {
                  "color": "#37872D",
                  "value": 0
                },
                {
                  "color": "#299c46",
                  "value": 1
                }
              ]
            },
            "unit": "none"
          },
          "overrides": []
        },
        "gridPos": {
          "h": 4,
          "w": 4,
          "x": 4,
          "y": 1
        },
        "id": 233,
        "links": [],
        "maxDataPoints": 100,
        "options": {
          "colorMode": "value",
          "graphMode": "area",
          "justifyMode": "auto",
          "orientation": "horizontal",
          "reduceOptions": {
            "calcs": [
              "lastNotNull"
            ],
            "fields": "",
            "values": false
          },
          "textMode": "auto"
        },
        "pluginVersion": "8.4.5",
        "repeatDirection": "h",
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "sum(kafka_controller_activecontrollercount{})",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "",
            "refId": "A"
          }
        ],
        "title": "Active Controllers",
        "type": "stat"
      },
      {
        "description": "",
        "fieldConfig": {
          "defaults": {
            "color": {
              "mode": "thresholds"
            },
            "mappings": [
              {
                "options": {
                  "match": "null",
                  "result": {
                    "text": "N/A"
                  }
                },
                "type": "special"
              }
            ],
            "thresholds": {
              "mode": "absolute",
              "steps": [
                {
                  "color": "green",
                  "value": null
                },
                {
                  "color": "red",
                  "value": 80
                }
              ]
            },
            "unit": "none"
          },
          "overrides": []
        },
        "gridPos": {
          "h": 4,
          "w": 4,
          "x": 8,
          "y": 1
        },
        "id": 625,
        "links": [],
        "maxDataPoints": 100,
        "options": {
          "colorMode": "value",
          "graphMode": "area",
          "justifyMode": "auto",
          "orientation": "horizontal",
          "reduceOptions": {
            "calcs": [
              "lastNotNull"
            ],
            "fields": "",
            "values": false
          },
          "textMode": "auto"
        },
        "pluginVersion": "8.4.5",
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "sum(kafka_controller_globaltopiccount{})",
            "format": "time_series",
            "hide": false,
            "interval": "",
            "intervalFactor": 2,
            "legendFormat": "",
            "refId": "A"
          }
        ],
        "title": "Total of Topics",
        "type": "stat"
      },
      {
        "description": "",
        "fieldConfig": {
          "defaults": {
            "color": {
              "mode": "thresholds"
            },
            "mappings": [
              {
                "options": {
                  "match": "null",
                  "result": {
                    "text": "N/A"
                  }
                },
                "type": "special"
              }
            ],
            "thresholds": {
              "mode": "absolute",
              "steps": [
                {
                  "color": "#508642",
                  "value": null
                },
                {
                  "color": "rgba(237, 129, 40, 0.89)",
                  "value": 1
                },
                {
                  "color": "#bf1b00",
                  "value": 5
                }
              ]
            },
            "unit": "none"
          },
          "overrides": []
        },
        "gridPos": {
          "h": 4,
          "w": 4,
          "x": 12,
          "y": 1
        },
        "id": 30,
        "links": [],
        "maxDataPoints": 100,
        "options": {
          "colorMode": "value",
          "graphMode": "area",
          "justifyMode": "auto",
          "orientation": "horizontal",
          "reduceOptions": {
            "calcs": [
              "lastNotNull"
            ],
            "fields": "",
            "values": false
          },
          "textMode": "auto"
        },
        "pluginVersion": "8.4.5",
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "sum(kafka_server_replica_manager_underreplicatedpartitions{})",
            "format": "time_series",
            "hide": false,
            "interval": "",
            "intervalFactor": 2,
            "legendFormat": "",
            "refId": "A"
          }
        ],
        "title": "Under Replicated Partitions",
        "type": "stat"
      },
      {
        "description": "",
        "fieldConfig": {
          "defaults": {
            "color": {
              "mode": "thresholds"
            },
            "mappings": [
              {
                "options": {
                  "match": "null",
                  "result": {
                    "text": "N/A"
                  }
                },
                "type": "special"
              }
            ],
            "thresholds": {
              "mode": "absolute",
              "steps": [
                {
                  "color": "#d44a3a",
                  "value": null
                },
                {
                  "color": "rgba(237, 129, 40, 0.89)",
                  "value": 0
                },
                {
                  "color": "#299c46",
                  "value": 0
                }
              ]
            },
            "unit": "none"
          },
          "overrides": []
        },
        "gridPos": {
          "h": 4,
          "w": 4,
          "x": 16,
          "y": 1
        },
        "id": 40,
        "links": [],
        "maxDataPoints": 100,
        "options": {
          "colorMode": "value",
          "graphMode": "area",
          "justifyMode": "auto",
          "orientation": "horizontal",
          "reduceOptions": {
            "calcs": [
              "lastNotNull"
            ],
            "fields": "",
            "values": false
          },
          "textMode": "auto"
        },
        "pluginVersion": "8.4.5",
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "sum(kafka_server_replica_manager_partitioncount{})",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "",
            "refId": "A"
          }
        ],
        "title": "Online Partitions",
        "type": "stat"
      },
      {
        "description": "",
        "fieldConfig": {
          "defaults": {
            "color": {
              "mode": "thresholds"
            },
            "mappings": [
              {
                "options": {
                  "match": "null",
                  "result": {
                    "text": "N/A"
                  }
                },
                "type": "special"
              }
            ],
            "thresholds": {
              "mode": "absolute",
              "steps": [
                {
                  "color": "#508642",
                  "value": null
                },
                {
                  "color": "rgba(237, 129, 40, 0.89)",
                  "value": 1
                },
                {
                  "color": "#bf1b00",
                  "value": 5
                }
              ]
            },
            "unit": "none"
          },
          "overrides": []
        },
        "gridPos": {
          "h": 4,
          "w": 4,
          "x": 20,
          "y": 1
        },
        "id": 126,
        "links": [],
        "maxDataPoints": 100,
        "options": {
          "colorMode": "value",
          "graphMode": "area",
          "justifyMode": "auto",
          "orientation": "horizontal",
          "reduceOptions": {
            "calcs": [
              "lastNotNull"
            ],
            "fields": "",
            "values": false
          },
          "textMode": "auto"
        },
        "pluginVersion": "8.4.5",
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "sum(kafka_controller_offlinepartitionscount{})",
            "format": "time_series",
            "hide": false,
            "interval": "",
            "intervalFactor": 2,
            "legendFormat": "",
            "refId": "A"
          }
        ],
        "title": "Offline Partitions",
        "type": "stat"
      },
      {
        "columns": [],
        "description": "",
        "fontSize": "100%",
        "gridPos": {
          "h": 10,
          "w": 9,
          "x": 0,
          "y": 5
        },
        "id": 622,
        "links": [],
        "scroll": true,
        "showHeader": true,
        "sort": {
          "col": 0,
          "desc": true
        },
        "styles": [
          {
            "alias": "Time",
            "align": "auto",
            "dateFormat": "YYYY-MM-DD HH:mm:ss",
            "pattern": "Time",
            "type": "hidden"
          },
          {
            "alias": "",
            "align": "auto",
            "colors": [
              "rgba(245, 54, 54, 0.9)",
              "rgba(237, 129, 40, 0.89)",
              "rgba(50, 172, 45, 0.97)"
            ],
            "decimals": 2,
            "pattern": "__name__",
            "thresholds": [],
            "type": "hidden",
            "unit": "short"
          },
          {
            "alias": " Brokers",
            "align": "auto",
            "colors": [
              "rgba(245, 54, 54, 0.9)",
              "rgba(237, 129, 40, 0.89)",
              "rgba(50, 172, 45, 0.97)"
            ],
            "dateFormat": "YYYY-MM-DD HH:mm:ss",
            "decimals": 2,
            "mappingType": 1,
            "pattern": "instance",
            "thresholds": [],
            "type": "string",
            "unit": "short"
          },
          {
            "alias": "",
            "align": "auto",
            "colorMode": "value",
            "colors": [
              "#FA6400",
              "#56A64B",
              "#FF780A"
            ],
            "dateFormat": "YYYY-MM-DD HH:mm:ss",
            "decimals": 2,
            "mappingType": 1,
            "pattern": "Value",
            "thresholds": [
              "1"
            ],
            "type": "string",
            "unit": "short",
            "valueMaps": [
              {
                "text": "Controller",
                "value": "1"
              },
              {
                "text": "Follower",
                "value": "0"
              }
            ]
          },
          {
            "alias": "",
            "align": "auto",
            "colors": [
              "rgba(245, 54, 54, 0.9)",
              "rgba(237, 129, 40, 0.89)",
              "rgba(50, 172, 45, 0.97)"
            ],
            "dateFormat": "YYYY-MM-DD HH:mm:ss",
            "decimals": 2,
            "mappingType": 1,
            "pattern": "job",
            "thresholds": [],
            "type": "hidden",
            "unit": "short"
          }
        ],
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": false,
            "expr": "kafka_controller_activecontrollercount{}",
            "format": "table",
            "instant": true,
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "",
            "refId": "A"
          }
        ],
        "title": "Controller and Followers ",
        "transform": "table",
        "type": "table-old"
      },
      {
        "fieldConfig": {
          "defaults": {
            "color": {
              "mode": "thresholds"
            },
            "displayName": "Messages In Per Sec",
            "mappings": [],
            "noValue": "0",
            "thresholds": {
              "mode": "absolute",
              "steps": [
                {
                  "color": "green",
                  "value": null
                }
              ]
            },
            "unit": "locale"
          },
          "overrides": []
        },
        "gridPos": {
          "h": 5,
          "w": 6,
          "x": 9,
          "y": 5
        },
        "id": 683,
        "options": {
          "colorMode": "background",
          "graphMode": "area",
          "justifyMode": "auto",
          "orientation": "auto",
          "reduceOptions": {
            "calcs": [
              "last"
            ],
            "fields": "",
            "values": false
          },
          "textMode": "auto"
        },
        "pluginVersion": "8.4.5",
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "sum(rate(kafka_server_broker_topic_metrics_messagesinpersec_rate{}[1m]))",
            "interval": "",
            "legendFormat": "Total messages in per sec ",
            "refId": "A"
          }
        ],
        "type": "stat"
      },
      {
        "columns": [],
        "description": "",
        "fontSize": "100%",
        "gridPos": {
          "h": 10,
          "w": 9,
          "x": 15,
          "y": 5
        },
        "id": 619,
        "links": [],
        "scroll": true,
        "showHeader": true,
        "sort": {
          "col": 0,
          "desc": true
        },
        "styles": [
          {
            "$$hashKey": "object:45",
            "alias": "Time",
            "align": "auto",
            "dateFormat": "YYYY-MM-DD HH:mm:ss",
            "pattern": "Time",
            "type": "hidden"
          },
          {
            "$$hashKey": "object:46",
            "alias": "",
            "align": "auto",
            "colors": [
              "rgba(245, 54, 54, 0.9)",
              "rgba(237, 129, 40, 0.89)",
              "rgba(50, 172, 45, 0.97)"
            ],
            "decimals": 2,
            "pattern": "__name__",
            "thresholds": [],
            "type": "hidden",
            "unit": "short"
          },
          {
            "$$hashKey": "object:47",
            "alias": "Brokers",
            "align": "auto",
            "colors": [
              "rgba(245, 54, 54, 0.9)",
              "rgba(237, 129, 40, 0.89)",
              "rgba(50, 172, 45, 0.97)"
            ],
            "dateFormat": "YYYY-MM-DD HH:mm:ss",
            "decimals": 2,
            "mappingType": 1,
            "pattern": "instance",
            "thresholds": [],
            "type": "string",
            "unit": "short"
          },
          {
            "$$hashKey": "object:48",
            "alias": "Leader ",
            "align": "auto",
            "colorMode": "value",
            "colors": [
              "#FA6400",
              "#56A64B",
              "#FF780A"
            ],
            "dateFormat": "YYYY-MM-DD HH:mm:ss",
            "decimals": 2,
            "mappingType": 1,
            "pattern": "Value #A",
            "thresholds": [
              "1"
            ],
            "type": "string",
            "unit": "short",
            "valueMaps": []
          },
          {
            "$$hashKey": "object:49",
            "alias": "",
            "align": "auto",
            "colors": [
              "rgba(245, 54, 54, 0.9)",
              "rgba(237, 129, 40, 0.89)",
              "rgba(50, 172, 45, 0.97)"
            ],
            "dateFormat": "YYYY-MM-DD HH:mm:ss",
            "decimals": 2,
            "mappingType": 1,
            "pattern": "job",
            "thresholds": [],
            "type": "hidden",
            "unit": "short"
          },
          {
            "$$hashKey": "object:50",
            "alias": "Replicas",
            "align": "auto",
            "colorMode": "value",
            "colors": [
              "rgba(50, 172, 45, 0.97)",
              "rgba(237, 129, 40, 0.89)",
              "rgba(245, 54, 54, 0.9)"
            ],
            "dateFormat": "YYYY-MM-DD HH:mm:ss",
            "decimals": 2,
            "mappingType": 1,
            "pattern": "Value #B",
            "thresholds": [],
            "type": "string",
            "unit": "short"
          },
          {
            "$$hashKey": "object:51",
            "alias": "Leader Percent",
            "align": "auto",
            "colorMode": "value",
            "colors": [
              "rgba(245, 54, 54, 0.9)",
              "rgba(237, 129, 40, 0.89)",
              "rgba(50, 172, 45, 0.97)"
            ],
            "dateFormat": "YYYY-MM-DD HH:mm:ss",
            "decimals": 2,
            "mappingType": 1,
            "pattern": "Value #C",
            "thresholds": [
              "20",
              "30",
              "40"
            ],
            "type": "number",
            "unit": "percent"
          }
        ],
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": false,
            "expr": "(kafka_server_replica_manager_leadercount{instance=\"jmx-kafka101:5556\", job=\"kafka\"} / kafka_server_replica_manager_partitioncount\n{instance=\"jmx-kafka101:5556\", job=\"kafka\"}) * 100",
            "format": "table",
            "hide": false,
            "instant": true,
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "",
            "refId": "C"
          },
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": false,
            "expr": "kafka_server_replica_manager_leadercount{instance=\"jmx-kafka101:5556\", job=\"kafka\"}",
            "format": "table",
            "hide": false,
            "instant": true,
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "",
            "refId": "A"
          },
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": false,
            "expr": "count(kafka_cluster_partition_replicascount{instance=\"jmx-kafka101:5556\", job=\"kafka\"} <= 1)by(instance)",
            "format": "table",
            "instant": true,
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "",
            "refId": "B"
          }
        ],
        "title": "Partitions Leader and Replica Per Broker",
        "transform": "table",
        "type": "table-old"
      },
      {
        "fieldConfig": {
          "defaults": {
            "color": {
              "mode": "thresholds"
            },
            "displayName": "Messages In Per Sec",
            "mappings": [],
            "noValue": "0",
            "thresholds": {
              "mode": "absolute",
              "steps": [
                {
                  "color": "green",
                  "value": null
                }
              ]
            },
            "unit": "locale"
          },
          "overrides": []
        },
        "gridPos": {
          "h": 5,
          "w": 6,
          "x": 9,
          "y": 10
        },
        "id": 688,
        "options": {
          "colorMode": "background",
          "graphMode": "area",
          "justifyMode": "auto",
          "orientation": "auto",
          "reduceOptions": {
            "calcs": [
              "last"
            ],
            "fields": "",
            "values": false
          },
          "textMode": "auto"
        },
        "pluginVersion": "8.4.5",
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "sum(increase(kafka_server_broker_topic_metrics_messagesinpersec_rate{}[$__range]))",
            "interval": "",
            "legendFormat": "Total messages from ${__from:date:MM-DD hA} to ${__to:date:MM-DD hA}",
            "refId": "A"
          }
        ],
        "type": "stat"
      },
      {
        "description": "",
        "fieldConfig": {
          "defaults": {
            "decimals": 2,
            "displayName": "Broker: $broker",
            "mappings": [
              {
                "options": {
                  "match": "null",
                  "result": {
                    "text": "N/A"
                  }
                },
                "type": "special"
              }
            ],
            "max": 100,
            "min": 0,
            "thresholds": {
              "mode": "absolute",
              "steps": [
                {
                  "color": "#299c46",
                  "value": null
                },
                {
                  "color": "rgba(237, 129, 40, 0.89)",
                  "value": 80
                },
                {
                  "color": "#d44a3a",
                  "value": 90
                }
              ]
            },
            "unit": "percent"
          },
          "overrides": []
        },
        "gridPos": {
          "h": 5,
          "w": 8,
          "x": 0,
          "y": 15
        },
        "id": 467,
        "links": [],
        "options": {
          "orientation": "horizontal",
          "reduceOptions": {
            "calcs": [
              "lastNotNull"
            ],
            "fields": "",
            "values": false
          },
          "showThresholdLabels": false,
          "showThresholdMarkers": true
        },
        "pluginVersion": "8.4.5",
        "repeat": "broker",
        "repeatDirection": "h",
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "100 - (kafka_network_socket_server_processor_avg_idle_percent{}*100)",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "Network processor avg {{instance}}",
            "refId": "A"
          }
        ],
        "type": "gauge"
      },
      {
        "collapsed": true,
        "datasource": {
          "type": "prometheus",
          "uid": "OYKLxrO4k"
        },
        "gridPos": {
          "h": 1,
          "w": 24,
          "x": 0,
          "y": 20
        },
        "id": 680,
        "panels": [
          {
            "description": "If <= 0 is very idle",
            "fieldConfig": {
              "defaults": {
                "decimals": 2,
                "displayName": "Broker: $broker",
                "mappings": [
                  {
                    "options": {
                      "match": "null",
                      "result": {
                        "text": "N/A"
                      }
                    },
                    "type": "special"
                  }
                ],
                "max": 100,
                "min": 0,
                "noValue": "0",
                "thresholds": {
                  "mode": "absolute",
                  "steps": [
                    {
                      "color": "#299c46"
                    },
                    {
                      "color": "rgba(237, 129, 40, 0.89)",
                      "value": 80
                    },
                    {
                      "color": "#d44a3a",
                      "value": 90
                    }
                  ]
                },
                "unit": "percent"
              },
              "overrides": []
            },
            "gridPos": {
              "h": 5,
              "w": 8,
              "x": 0,
              "y": 21
            },
            "id": 681,
            "links": [],
            "maxPerRow": 6,
            "options": {
              "orientation": "horizontal",
              "reduceOptions": {
                "calcs": [
                  "lastNotNull"
                ],
                "fields": "",
                "values": false
              },
              "showThresholdLabels": false,
              "showThresholdMarkers": true
            },
            "pluginVersion": "8.4.5",
            "repeat": "broker",
            "repeatDirection": "h",
            "targets": [
              {
                "datasource": {
                  "type": "prometheus",
                  "uid": "OYKLxrO4k"
                },
                "exemplar": true,
                "expr": "100 - rate(kafka_server_request_handler_avg_idle_percent{job=\"kafka\",instance= \"jmx-kafka101:5556\"}[1m]) / 10000000",
                "format": "time_series",
                "instant": false,
                "interval": "",
                "intervalFactor": 1,
                "legendFormat": "Request handler avg {{instance}}",
                "refId": "A"
              }
            ],
            "type": "gauge"
          }
        ],
        "title": "Request Handler",
        "type": "row"
      },
      {
        "collapsed": false,
        "datasource": {
          "type": "prometheus",
          "uid": "OYKLxrO4k"
        },
        "gridPos": {
          "h": 1,
          "w": 24,
          "x": 0,
          "y": 21
        },
        "id": 651,
        "panels": [],
        "title": "Latency",
        "type": "row"
      },
      {
        "description": "",
        "fieldConfig": {
          "defaults": {
            "color": {
              "mode": "thresholds"
            },
            "displayName": "Total Time Produce Latency 99th",
            "mappings": [],
            "max": "1000",
            "min": 0,
            "thresholds": {
              "mode": "absolute",
              "steps": [
                {
                  "color": "#7EB26D",
                  "index": 0,
                  "value": null
                },
                {
                  "color": "#E0B400",
                  "index": 1,
                  "value": 500
                },
                {
                  "color": "#C4162A",
                  "index": 2,
                  "value": 800
                }
              ]
            },
            "unit": "ms"
          },
          "overrides": []
        },
        "gridPos": {
          "h": 5,
          "w": 8,
          "x": 0,
          "y": 22
        },
        "id": 192,
        "links": [],
        "maxPerRow": 6,
        "options": {
          "orientation": "auto",
          "reduceOptions": {
            "calcs": [
              "lastNotNull"
            ],
            "fields": "",
            "values": false
          },
          "showThresholdLabels": false,
          "showThresholdMarkers": true
        },
        "pluginVersion": "8.4.5",
        "repeatDirection": "h",
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "avg(kafka_network_request_metrics_time_ms{request=\"Produce\",job=\"kafka\",aggregate=\"99thPercentile\",instance=\"jmx-kafka101:5556\"})by(request)",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "Total {{request}} 99th",
            "refId": "D"
          }
        ],
        "type": "gauge"
      },
      {
        "description": "",
        "fieldConfig": {
          "defaults": {
            "color": {
              "mode": "thresholds"
            },
            "displayName": "Total Time FetchConsumer Latency 99th",
            "mappings": [],
            "max": "1000",
            "min": 0,
            "thresholds": {
              "mode": "absolute",
              "steps": [
                {
                  "color": "#7EB26D",
                  "value": null
                },
                {
                  "color": "#E0B400",
                  "value": 600
                },
                {
                  "color": "#C4162A",
                  "value": 800
                }
              ]
            },
            "unit": "ms"
          },
          "overrides": []
        },
        "gridPos": {
          "h": 5,
          "w": 8,
          "x": 8,
          "y": 22
        },
        "id": 677,
        "links": [],
        "maxPerRow": 6,
        "options": {
          "orientation": "auto",
          "reduceOptions": {
            "calcs": [
              "lastNotNull"
            ],
            "fields": "",
            "values": false
          },
          "showThresholdLabels": false,
          "showThresholdMarkers": true
        },
        "pluginVersion": "8.4.5",
        "repeatDirection": "h",
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "avg(kafka_network_request_metrics_time_ms{request=\"FetchConsumer\",job=\"kafka\",aggregate=\"99thPercentile\",instance=\"jmx-kafka101:5556\"})by(request)",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "Total {{request}} 99th",
            "refId": "D"
          }
        ],
        "type": "gauge"
      },
      {
        "description": "",
        "fieldConfig": {
          "defaults": {
            "color": {
              "mode": "thresholds"
            },
            "displayName": "Total Time FetchFollower Latency 99th",
            "mappings": [],
            "max": "1000",
            "min": 0,
            "thresholds": {
              "mode": "absolute",
              "steps": [
                {
                  "color": "#7EB26D",
                  "value": null
                },
                {
                  "color": "#E0B400",
                  "value": 599
                },
                {
                  "color": "#C4162A",
                  "value": 800
                }
              ]
            },
            "unit": "ms"
          },
          "overrides": []
        },
        "gridPos": {
          "h": 5,
          "w": 8,
          "x": 16,
          "y": 22
        },
        "id": 678,
        "links": [],
        "maxPerRow": 6,
        "options": {
          "orientation": "auto",
          "reduceOptions": {
            "calcs": [
              "lastNotNull"
            ],
            "fields": "",
            "values": false
          },
          "showThresholdLabels": false,
          "showThresholdMarkers": true
        },
        "pluginVersion": "8.4.5",
        "repeatDirection": "h",
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "avg(kafka_network_request_metrics_time_ms{request=\"FetchFollower\",job=\"kafka\",aggregate=\"99thPercentile\",instance=\"jmx-kafka101:5556\"})by(request)",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "Total {{request}} 99th",
            "refId": "D"
          }
        ],
        "type": "gauge"
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 1,
        "fillGradient": 0,
        "gridPos": {
          "h": 8,
          "w": 8,
          "x": 0,
          "y": 27
        },
        "hiddenSeries": false,
        "id": 665,
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "max": true,
          "min": true,
          "show": true,
          "sort": "current",
          "sortDesc": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 1,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 2,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "avg(kafka_network_request_metrics_time_ms{request=\"Produce\",job=\"kafka\",aggregate=\"99thPercentile\",instance=\"jmx-kafka101:5556\"})by(instance)",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "{{instance}}",
            "refId": "D"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "Produce Latency 99th per Broker",
        "tooltip": {
          "shared": true,
          "sort": 2,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "format": "ms",
            "logBase": 1,
            "show": true
          },
          {
            "format": "short",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 1,
        "fillGradient": 0,
        "gridPos": {
          "h": 8,
          "w": 8,
          "x": 8,
          "y": 27
        },
        "hiddenSeries": false,
        "id": 666,
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "max": true,
          "min": true,
          "show": true,
          "sort": "current",
          "sortDesc": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 1,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 2,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "avg(kafka_network_request_metrics_time_ms{request=\"FetchConsumer\",job=\"kafka\",aggregate=\"99thPercentile\",instance=\"jmx-kafka101:5556\"})by(instance)",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "{{instance}}",
            "refId": "D"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "FetchConsumer Latency 99th per Broker",
        "tooltip": {
          "shared": true,
          "sort": 2,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "format": "ms",
            "logBase": 1,
            "show": true
          },
          {
            "format": "short",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 1,
        "fillGradient": 0,
        "gridPos": {
          "h": 8,
          "w": 8,
          "x": 16,
          "y": 27
        },
        "hiddenSeries": false,
        "id": 667,
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "max": true,
          "min": true,
          "show": true,
          "sort": "current",
          "sortDesc": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 1,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 2,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "avg(kafka_network_request_metrics_time_ms{request=\"FetchFollower\",job=\"kafka\",aggregate=\"99thPercentile\",instance=\"jmx-kafka101:5556\"})by(instance)",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "{{instance}}",
            "refId": "D"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "FetchFollow Latency 99th per Broker",
        "tooltip": {
          "shared": true,
          "sort": 2,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "format": "ms",
            "logBase": 1,
            "show": true
          },
          {
            "format": "short",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "collapsed": false,
        "datasource": {
          "type": "prometheus",
          "uid": "OYKLxrO4k"
        },
        "gridPos": {
          "h": 1,
          "w": 24,
          "x": 0,
          "y": 35
        },
        "id": 653,
        "panels": [],
        "title": "Throughput",
        "type": "row"
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 0,
        "fillGradient": 0,
        "gridPos": {
          "h": 10,
          "w": 12,
          "x": 0,
          "y": 36
        },
        "hiddenSeries": false,
        "id": 152,
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "max": true,
          "min": true,
          "rightSide": true,
          "show": true,
          "sort": "current",
          "sortDesc": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 2,
        "links": [],
        "nullPointMode": "null as zero",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 5,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "\nsort(sum(rate(kafka_server_broker_topic_metrics_messagesinpersec_rate{aggregate=\"OneMinute\", env=\"cluster-demo\", instance=\"jmx-kafka101:5556\", job=\"kafka\", service=\"kafka-broker\",topic!=\"\"}[1m]))by(topic))\n#sort(sum(rate(kafka_server_brokertopicmetrics_messagesin_total{job=\"kafka\",instance=~\"jmx-kafka101:5556\",topic!=\"\",topic=~\"$topic\"}[1m]))by(topic))\n",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "Topic: {{topic}}",
            "refId": "D"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "Messages In Per Topic",
        "tooltip": {
          "shared": false,
          "sort": 0,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "format": "reqps",
            "label": "Message/s",
            "logBase": 1,
            "show": true
          },
          {
            "format": "short",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 0,
        "fillGradient": 0,
        "gridPos": {
          "h": 10,
          "w": 12,
          "x": 12,
          "y": 36
        },
        "hiddenSeries": false,
        "id": 155,
        "interval": "",
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "hideEmpty": false,
          "hideZero": false,
          "max": true,
          "min": true,
          "rightSide": true,
          "show": true,
          "sort": "current",
          "sortDesc": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 2,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 5,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "sum(rate(kafka_server_broker_topic_metrics_bytesinpersec_rate{aggregate=\"OneMinute\", env=\"cluster-demo\", instance=\"jmx-kafka101:5556\", job=\"kafka\", service=\"kafka-broker\", topic!=\"\"}[1m]))by(topic)",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 2,
            "legendFormat": "Topic: {{topic}}",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "Bytes In Per Topic",
        "tooltip": {
          "shared": false,
          "sort": 0,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "format": "Bps",
            "label": "Bytes/s",
            "logBase": 1,
            "show": true
          },
          {
            "format": "Bps",
            "label": "",
            "logBase": 1,
            "show": false
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 1,
        "fillGradient": 0,
        "gridPos": {
          "h": 10,
          "w": 12,
          "x": 0,
          "y": 46
        },
        "hiddenSeries": false,
        "id": 142,
        "interval": "",
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "hideEmpty": false,
          "hideZero": false,
          "max": true,
          "min": true,
          "rightSide": true,
          "show": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 2,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 5,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [
          {
            "$$hashKey": "object:411",
            "alias": "/.*Bytes In*./",
            "transform": "negative-Y"
          }
        ],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "sum (rate(kafka_server_broker_topic_metrics_bytesoutpersec_rate{aggregate=\"OneMinute\", env=\"cluster-demo\", instance=\"jmx-kafka101:5556\", job=\"kafka\", service=\"kafka-broker\", topic!=\"\"}[1m]))by(instance)\n\n#sum (rate(kafka_server_brokertopicmetrics_bytesout_total{job=\"$job\",instance=~\"$broker\",topic!=\"\"}[1m]))by(instance)",
            "format": "time_series",
            "instant": false,
            "interval": "",
            "intervalFactor": 2,
            "legendFormat": "Bytes Out [{{instance}}]",
            "refId": "B"
          },
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "sum(rate(kafka_server_broker_topic_metrics_bytesinpersec_rate{aggregate=\"OneMinute\", env=\"cluster-demo\", instance=\"jmx-kafka101:5556\", job=\"kafka\", service=\"kafka-broker\", topic!=\"\"}[1m]))by(instance)\n#sum (rate(kafka_server_brokertopicmetrics_bytesin_total{job=\"$job\",instance=~\"$broker\",topic!=\"\"}[1m]))by(instance)",
            "format": "time_series",
            "instant": false,
            "interval": "",
            "intervalFactor": 2,
            "legendFormat": "Bytes In [{{instance}}]",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "Bytes In / Out Per Broker",
        "tooltip": {
          "shared": true,
          "sort": 0,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "$$hashKey": "object:424",
            "format": "Bps",
            "label": "In (-) / Out (+)",
            "logBase": 1,
            "show": true
          },
          {
            "$$hashKey": "object:425",
            "format": "Bps",
            "label": "",
            "logBase": 1,
            "show": false
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "aliasColors": {
          "Incoming Byte Topic: depositos-comando-ledger": "light-orange"
        },
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 0,
        "fillGradient": 0,
        "gridPos": {
          "h": 10,
          "w": 12,
          "x": 12,
          "y": 46
        },
        "hiddenSeries": false,
        "id": 154,
        "interval": "",
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "hideEmpty": false,
          "hideZero": false,
          "max": true,
          "min": true,
          "rightSide": true,
          "show": true,
          "sort": "current",
          "sortDesc": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 2,
        "links": [],
        "nullPointMode": "connected",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 5,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "sum (rate(kafka_server_broker_topic_metrics_bytesoutpersec_rate{aggregate=\"OneMinute\", env=\"cluster-demo\", instance=\"jmx-kafka101:5556\", job=\"kafka\", service=\"kafka-broker\", topic!=\"\"}[1m]))by(topic)",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 2,
            "legendFormat": "Topic: {{topic}}",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "Bytes Out Per Topic",
        "tooltip": {
          "shared": false,
          "sort": 0,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "format": "Bps",
            "label": "Bytes/s",
            "logBase": 1,
            "show": true
          },
          {
            "format": "Bps",
            "label": "",
            "logBase": 1,
            "show": false
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "aliasColors": {
          "Failed Produce Request Broker - 10.24.88.7:9091": "dark-red",
          "Failed Produce Request Broker - 10.24.88.8:9091": "semi-dark-red",
          "Failed Produce Request Broker - 10.24.88.9:9091": "light-red",
          "Total Produce Request Broker - 10.24.88.7:9091": "dark-green",
          "Total Produce Request Broker - 10.24.88.8:9091": "semi-dark-green",
          "Total Produce Request Broker - 10.24.88.9:9091": "light-green"
        },
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "datasource": {
          "type": "prometheus",
          "uid": "OYKLxrO4k"
        },
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 0,
        "fillGradient": 0,
        "gridPos": {
          "h": 10,
          "w": 12,
          "x": 0,
          "y": 56
        },
        "hiddenSeries": false,
        "id": 50,
        "interval": "",
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "max": true,
          "min": true,
          "rightSide": true,
          "show": true,
          "sort": "current",
          "sortDesc": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 2,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 5,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "expr": "sum (rate(kafka_server_brokertopicmetrics_totalproducerequests_total{job=\"$job\",instance=~\"$broker\",topic!=\"\",topic=~\"$topic\"}[1m]))by(topic)",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "Topic: {{topic}}",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "Total Produce Request Rate Per Topic",
        "tooltip": {
          "shared": false,
          "sort": 0,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "format": "reqps",
            "label": "Request/s",
            "logBase": 1,
            "show": true
          },
          {
            "format": "reqps",
            "label": "",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "datasource": {
          "type": "prometheus",
          "uid": "OYKLxrO4k"
        },
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 0,
        "fillGradient": 0,
        "gridPos": {
          "h": 10,
          "w": 12,
          "x": 12,
          "y": 56
        },
        "hiddenSeries": false,
        "id": 176,
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "max": true,
          "min": true,
          "rightSide": true,
          "show": true,
          "sort": "current",
          "sortDesc": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 2,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 5,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "expr": "sum(rate(kafka_network_requestmetrics_requests_total{request=~\"Produce\",job=\"$job\",instance=~\"$broker\"}[1m]))by(instance)",
            "format": "time_series",
            "instant": false,
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "Request: {{instance}}",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "Produce Request Per Broker",
        "tooltip": {
          "shared": true,
          "sort": 1,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "format": "reqps",
            "label": "Request/s",
            "logBase": 1,
            "show": true
          },
          {
            "format": "short",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "collapsed": false,
        "datasource": {
          "type": "prometheus",
          "uid": "OYKLxrO4k"
        },
        "gridPos": {
          "h": 1,
          "w": 24,
          "x": 0,
          "y": 66
        },
        "id": 28,
        "panels": [],
        "title": "Troubleshooting",
        "type": "row"
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "datasource": {
          "type": "prometheus",
          "uid": "OYKLxrO4k"
        },
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 0,
        "fillGradient": 0,
        "gridPos": {
          "h": 9,
          "w": 12,
          "x": 0,
          "y": 67
        },
        "hiddenSeries": false,
        "id": 612,
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "max": true,
          "min": false,
          "rightSide": true,
          "show": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 2,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 5,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "expr": "sum(irate(kafka_server_brokertopicmetrics_failedproducerequests_total{job=~\"$job\",instance=~\"$broker\"}[1m]))by(instance)",
            "format": "time_series",
            "instant": false,
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "{{instance}}",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "Failed Produce Request Per Broker",
        "tooltip": {
          "shared": true,
          "sort": 1,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "format": "reqps",
            "label": "Request/s",
            "logBase": 1,
            "show": true
          },
          {
            "format": "short",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "datasource": {
          "type": "prometheus",
          "uid": "OYKLxrO4k"
        },
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 0,
        "fillGradient": 0,
        "gridPos": {
          "h": 9,
          "w": 12,
          "x": 12,
          "y": 67
        },
        "hiddenSeries": false,
        "id": 613,
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "max": true,
          "min": false,
          "rightSide": true,
          "show": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 2,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 5,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "expr": "sum(irate(kafka_server_brokertopicmetrics_failedfetchrequests_total{job=~\"$job\",instance=~\"$broker\"}[1m]))by(instance)",
            "format": "time_series",
            "instant": false,
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "{{instance}}",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "Failed Fetch Request Per Broker",
        "tooltip": {
          "shared": true,
          "sort": 1,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "format": "reqps",
            "label": "Request/s",
            "logBase": 1,
            "show": true
          },
          {
            "format": "short",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "datasource": {
          "type": "prometheus",
          "uid": "OYKLxrO4k"
        },
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 0,
        "fillGradient": 0,
        "gridPos": {
          "h": 9,
          "w": 12,
          "x": 0,
          "y": 76
        },
        "hiddenSeries": false,
        "id": 614,
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "max": true,
          "min": false,
          "rightSide": true,
          "show": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 2,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 5,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "expr": "sum(irate(kafka_server_brokertopicmetrics_failedproducerequests_total{job=~\"$job\",topic!=\"\",instance=~\"$broker\",topic=~\"$topic\"}[1m]))by(topic)",
            "format": "time_series",
            "instant": false,
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "{{topic}}",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "Failed Produce Request Per Topic",
        "tooltip": {
          "shared": false,
          "sort": 1,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "format": "reqps",
            "label": "Request/s",
            "logBase": 1,
            "show": true
          },
          {
            "format": "short",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "datasource": {
          "type": "prometheus",
          "uid": "OYKLxrO4k"
        },
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 0,
        "fillGradient": 0,
        "gridPos": {
          "h": 9,
          "w": 12,
          "x": 12,
          "y": 76
        },
        "hiddenSeries": false,
        "id": 615,
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "max": true,
          "min": false,
          "rightSide": true,
          "show": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 2,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 5,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "expr": "sum(irate(kafka_server_brokertopicmetrics_failedfetchrequests_total{job=~\"$job\",topic!=\"\",instance=~\"$broker\",topic=~\"$topic\"}[1m]))by(topic)",
            "format": "time_series",
            "instant": false,
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "{{topic}}",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "Failed Fetch Request Per Topic",
        "tooltip": {
          "shared": false,
          "sort": 1,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "$$hashKey": "object:947",
            "format": "reqps",
            "label": "Request/s",
            "logBase": 1,
            "show": true
          },
          {
            "$$hashKey": "object:948",
            "format": "short",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 1,
        "fillGradient": 0,
        "gridPos": {
          "h": 8,
          "w": 8,
          "x": 0,
          "y": 85
        },
        "hiddenSeries": false,
        "id": 138,
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "max": true,
          "min": true,
          "rightSide": false,
          "show": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 1,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 5,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "\nsum(rate(kafka_zookeeper_session_expire_listener_zookeeperdisconnectspersec{aggregate=\"OneMinute\",env=\"cluster-demo\", instance=\"jmx-kafka101:5556\", job=\"kafka\", service=\"kafka-broker\"}[1m]))by(instance)\n#sum(rate(kafka_server_sessionexpirelistener_zookeeperdisconnects_total{job=\"$job\",instance=~\"$broker\"}[1m]))by(instance)",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "Broker - {{instance}}",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "ZooKeeper Disconnects Per Sec",
        "tooltip": {
          "shared": true,
          "sort": 0,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "format": "ms",
            "label": "Time/ms",
            "logBase": 1,
            "show": true
          },
          {
            "format": "short",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 1,
        "fillGradient": 0,
        "gridPos": {
          "h": 8,
          "w": 8,
          "x": 8,
          "y": 85
        },
        "hiddenSeries": false,
        "id": 139,
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "max": true,
          "min": true,
          "rightSide": false,
          "show": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 1,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 5,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "sum(kafka_zookeeper_session_expire_listener_zookeeperexpirespersec{aggregate=\"OneMinute\", env=\"cluster-demo\", instance=\"jmx-kafka101:5556\", job=\"kafka\", service=\"kafka-broker\"})by(instance)\n#sum (irate(kafka_server_sessionexpirelistener_zookeeperexpires_total{job=\"$job\",instance=~\"$broker\"}[1m]))by(instance)",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "Broker - {{instance}}",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "ZooKeeper Expires Per Sec",
        "tooltip": {
          "shared": true,
          "sort": 0,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "$$hashKey": "object:1050",
            "format": "ms",
            "label": "Time/ms",
            "logBase": 1,
            "show": true
          },
          {
            "$$hashKey": "object:1051",
            "format": "short",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "datasource": {
          "type": "prometheus",
          "uid": "OYKLxrO4k"
        },
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 1,
        "fillGradient": 0,
        "gridPos": {
          "h": 8,
          "w": 8,
          "x": 16,
          "y": 85
        },
        "hiddenSeries": false,
        "id": 150,
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "max": true,
          "min": true,
          "rightSide": false,
          "show": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 1,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 5,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "expr": "sum(kafka_server_zookeeperclientmetrics_zookeeperrequestlatencyms{job=\"$job\",instance=~\"$broker\"})by(instance)",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "Broker: {{instance}}",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "ZooKeeper Request Latency Ms",
        "tooltip": {
          "shared": true,
          "sort": 0,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "format": "ms",
            "label": "Time/ms",
            "logBase": 1,
            "show": true
          },
          {
            "format": "short",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 1,
        "fillGradient": 0,
        "gridPos": {
          "h": 10,
          "w": 12,
          "x": 0,
          "y": 93
        },
        "hiddenSeries": false,
        "id": 193,
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "hideEmpty": false,
          "hideZero": false,
          "max": true,
          "min": true,
          "rightSide": false,
          "show": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 2,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 5,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [
          {
            "alias": "/.*Expands*./",
            "transform": "negative-Y"
          }
        ],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "\nkafka_server_replica_manager_isrshrinkspersec{aggregate=\"OneMinute\", env=\"cluster-demo\", instance=\"jmx-kafka101:5556\", job=\"kafka\", service=\"kafka-broker\"}\n#sum (irate(kafka_server_replicamanager_isrshrinks_total{job=\"$job\",instance=~\"$broker\"}[1m]))",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "ISR Shrinks Per Sec",
            "refId": "A"
          },
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "kafka_server_replica_manager_isrexpandspersec{aggregate=\"OneMinute\", env=\"cluster-demo\", instance=\"jmx-kafka101:5556\", job=\"kafka\", service=\"kafka-broker\"}\n#sum (irate(kafka_server_replicamanager_isrexpands_total{job=\"$job\",instance=~\"$broker\"}[1m]))",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "ISR Expands Per Sec",
            "refId": "B"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "Isr Shrinks / Isr Expands Per Sec",
        "tooltip": {
          "shared": true,
          "sort": 0,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "format": "ops",
            "label": "Expands (-) / Shrinks (+)",
            "logBase": 1,
            "show": true
          },
          {
            "format": "short",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "datasource": {
          "type": "prometheus",
          "uid": "OYKLxrO4k"
        },
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 0,
        "fillGradient": 0,
        "gridPos": {
          "h": 10,
          "w": 12,
          "x": 12,
          "y": 93
        },
        "hiddenSeries": false,
        "id": 177,
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "max": true,
          "min": true,
          "rightSide": false,
          "show": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 2,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 5,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "expr": "sum(rate(kafka_network_requestmetrics_requests_total{request=~\"FetchFollower\",job=\"$job\",instance=~\"$broker\"}[1m]))by(instance)",
            "format": "time_series",
            "instant": false,
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "Request: {{instance}}",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "FetchFollower Request Per Broker",
        "tooltip": {
          "shared": true,
          "sort": 1,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "format": "reqps",
            "label": "Request/s",
            "logBase": 1,
            "show": true
          },
          {
            "format": "short",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "decimals": 0,
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 0,
        "fillGradient": 0,
        "gridPos": {
          "h": 8,
          "w": 12,
          "x": 0,
          "y": 103
        },
        "hiddenSeries": false,
        "id": 178,
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "max": true,
          "min": true,
          "rightSide": false,
          "show": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 2,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 5,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "kafka_network_request_per_sec{aggregate=\"Mean\", env=\"cluster-demo\", instance=\"jmx-kafka101:5556\", job=\"kafka\", request=\"FetchConsumer\", service=\"kafka-broker\", version=\"3\"}\n#sum(irate(kafka_network_requestmetrics_requests_total{request=\"FetchConsumer\",job=\"$job\",instance=~\"$broker\"}[5m]))by(instance)",
            "format": "time_series",
            "instant": false,
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "Request: {{instance}}",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "FetchConsumer Request Per Broker",
        "tooltip": {
          "shared": true,
          "sort": 1,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "$$hashKey": "object:1579",
            "decimals": 0,
            "format": "reqps",
            "label": "Request/s",
            "logBase": 1,
            "show": true
          },
          {
            "$$hashKey": "object:1580",
            "format": "short",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "datasource": {
          "type": "prometheus",
          "uid": "OYKLxrO4k"
        },
        "decimals": 0,
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 0,
        "fillGradient": 0,
        "gridPos": {
          "h": 8,
          "w": 12,
          "x": 12,
          "y": 103
        },
        "hiddenSeries": false,
        "id": 196,
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "hideEmpty": false,
          "hideZero": false,
          "max": true,
          "min": true,
          "rightSide": false,
          "show": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 2,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 5,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "expr": "sum (kafka_server_delayedoperationpurgatory_purgatorysize{job=\"$job\",delayedOperation=\"Fetch\",instance=~\"$broker\"})by(instance)",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "Broker {{instance}}",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "Number of Requests Waiting in the Fetch Purgatory",
        "tooltip": {
          "shared": true,
          "sort": 0,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "decimals": 0,
            "format": "none",
            "label": "",
            "logBase": 1,
            "show": true
          },
          {
            "format": "short",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "datasource": {
          "type": "prometheus",
          "uid": "OYKLxrO4k"
        },
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 0,
        "fillGradient": 0,
        "gridPos": {
          "h": 8,
          "w": 12,
          "x": 0,
          "y": 111
        },
        "hiddenSeries": false,
        "id": 56,
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "max": true,
          "min": true,
          "rightSide": false,
          "show": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 2,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 5,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "expr": "sum (irate(kafka_server_brokertopicmetrics_totalfetchrequests_total{job=\"$job\",instance=~\"$broker\",topic!=\"\"}[1m]))by(instance)",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "Broker: {{instance}}",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "Total Fetch Request Per Broker",
        "tooltip": {
          "shared": true,
          "sort": 0,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "format": "reqps",
            "label": "Bytes/s",
            "logBase": 1,
            "show": true
          },
          {
            "format": "short",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "datasource": {
          "type": "prometheus",
          "uid": "OYKLxrO4k"
        },
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 1,
        "fillGradient": 0,
        "gridPos": {
          "h": 8,
          "w": 12,
          "x": 12,
          "y": 111
        },
        "hiddenSeries": false,
        "id": 147,
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "max": true,
          "min": true,
          "rightSide": false,
          "show": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 2,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 5,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "expr": "sum (irate(kafka_log_logflushstats_logflushrateandtimems_count{job=\"$job\",instance=~\"$broker\"}[5m]))by(instance)",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "Broker - {{instance}}",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "Log Flush Stats Count",
        "tooltip": {
          "shared": true,
          "sort": 0,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "format": "ms",
            "label": "",
            "logBase": 1,
            "show": true
          },
          {
            "format": "short",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "datasource": {
          "type": "prometheus",
          "uid": "OYKLxrO4k"
        },
        "decimals": 0,
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 0,
        "fillGradient": 0,
        "gridPos": {
          "h": 9,
          "w": 12,
          "x": 0,
          "y": 119
        },
        "hiddenSeries": false,
        "id": 195,
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "hideEmpty": false,
          "hideZero": false,
          "max": true,
          "min": true,
          "rightSide": false,
          "show": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 2,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 5,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "expr": "sum (kafka_server_delayedoperationpurgatory_purgatorysize{job=\"$job\",delayedOperation=\"Produce\",instance=~\"$broker\"})by(instance)",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "Broker {{instance}}",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "Number of Requests Waiting in the Producer Purgatory",
        "tooltip": {
          "shared": true,
          "sort": 0,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "decimals": 0,
            "format": "none",
            "label": "",
            "logBase": 1,
            "show": true
          },
          {
            "decimals": 0,
            "format": "short",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "datasource": {
          "type": "prometheus",
          "uid": "OYKLxrO4k"
        },
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 1,
        "fillGradient": 0,
        "gridPos": {
          "h": 9,
          "w": 12,
          "x": 12,
          "y": 119
        },
        "hiddenSeries": false,
        "id": 140,
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "max": true,
          "min": true,
          "rightSide": false,
          "show": true,
          "sort": "max",
          "sortDesc": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 1,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 5,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "expr": "sum (irate(kafka_controller_controllerstats_leaderelectionrateandtimems_count{job=\"$job\",instance=~\"$broker\"}[1m]))by(instance)",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "Broker - {{instance}}",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "Leader Election Rate Count",
        "tooltip": {
          "shared": true,
          "sort": 0,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "format": "none",
            "label": "",
            "logBase": 1,
            "show": true
          },
          {
            "format": "short",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "columns": [],
        "description": "",
        "fontSize": "100%",
        "gridPos": {
          "h": 9,
          "w": 24,
          "x": 0,
          "y": 128
        },
        "id": 628,
        "links": [],
        "pageSize": 200,
        "scroll": true,
        "showHeader": true,
        "sort": {
          "col": 4,
          "desc": true
        },
        "styles": [
          {
            "$$hashKey": "object:1741",
            "alias": "Time",
            "align": "auto",
            "dateFormat": "YYYY-MM-DD HH:mm:ss",
            "pattern": "Time",
            "type": "hidden"
          },
          {
            "$$hashKey": "object:1742",
            "alias": "Instance",
            "align": "auto",
            "colors": [
              "rgba(245, 54, 54, 0.9)",
              "rgba(237, 129, 40, 0.89)",
              "rgba(50, 172, 45, 0.97)"
            ],
            "dateFormat": "YYYY-MM-DD HH:mm:ss",
            "decimals": 2,
            "mappingType": 1,
            "pattern": "instance",
            "thresholds": [],
            "type": "string",
            "unit": "short"
          },
          {
            "$$hashKey": "object:1743",
            "alias": "Status",
            "align": "auto",
            "colorMode": "value",
            "colors": [
              "#FA6400",
              "#56A64B",
              "#FF780A"
            ],
            "dateFormat": "YYYY-MM-DD HH:mm:ss",
            "decimals": 2,
            "mappingType": 1,
            "pattern": "Value",
            "thresholds": [
              "1"
            ],
            "type": "string",
            "unit": "short",
            "valueMaps": [
              {
                "$$hashKey": "object:1804",
                "text": "Leader",
                "value": "3"
              },
              {
                "$$hashKey": "object:1805",
                "text": "Follower",
                "value": "0"
              },
              {
                "$$hashKey": "object:1806",
                "text": "Leader",
                "value": "4"
              }
            ]
          },
          {
            "$$hashKey": "object:1744",
            "alias": "",
            "align": "auto",
            "colors": [
              "rgba(245, 54, 54, 0.9)",
              "rgba(237, 129, 40, 0.89)",
              "rgba(50, 172, 45, 0.97)"
            ],
            "dateFormat": "YYYY-MM-DD HH:mm:ss",
            "decimals": 2,
            "mappingType": 1,
            "pattern": "job",
            "thresholds": [],
            "type": "hidden",
            "unit": "short"
          },
          {
            "$$hashKey": "object:1745",
            "alias": "",
            "align": "auto",
            "colors": [
              "rgba(245, 54, 54, 0.9)",
              "rgba(237, 129, 40, 0.89)",
              "rgba(50, 172, 45, 0.97)"
            ],
            "dateFormat": "YYYY-MM-DD HH:mm:ss",
            "decimals": 2,
            "mappingType": 1,
            "pattern": "__name__",
            "thresholds": [],
            "type": "hidden",
            "unit": "short"
          }
        ],
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": false,
            "expr": "kafka_cluster_partition_replicascount{env=\"cluster-demo\", instance=\"jmx-kafka101:5556\", job=\"kafka\", partition=\"0\", service=\"kafka-broker\", topic!=\"\"}\n#kafka_cluster_partition_replicascount{job=~\"$job\",topic=~\"$topic\"}",
            "format": "table",
            "instant": true,
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "",
            "refId": "A"
          }
        ],
        "title": "Partitions Leader Per Broker",
        "transform": "table",
        "type": "table-old"
      },
      {
        "aliasColors": {},
        "bars": true,
        "dashLength": 10,
        "dashes": false,
        "decimals": 2,
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 0,
        "fillGradient": 0,
        "gridPos": {
          "h": 8,
          "w": 24,
          "x": 0,
          "y": 137
        },
        "hiddenSeries": false,
        "id": 609,
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "max": true,
          "min": true,
          "rightSide": true,
          "show": false,
          "total": false,
          "values": true
        },
        "lines": false,
        "linewidth": 2,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 5,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "sort(sum(kafka_log_size{env=\"cluster-demo\", instance=\"jmx-kafka101:5556\", job=\"kafka\", partition=\"0\", service=\"kafka-broker\", topic!=\"\"})by(instance))\n#sort(sum(kafka_log_log_size{job=~\"$job\",instance=~\"$broker\"})by(instance))",
            "format": "time_series",
            "instant": false,
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "Instance Broker:  {{instance}}",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "Disk Usage Segment Size",
        "tooltip": {
          "shared": false,
          "sort": 1,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "series",
          "show": true,
          "values": [
            "total"
          ]
        },
        "yaxes": [
          {
            "decimals": 2,
            "format": "bytes",
            "label": "",
            "logBase": 2,
            "show": true
          },
          {
            "format": "short",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "aliasColors": {},
        "bars": true,
        "dashLength": 10,
        "dashes": false,
        "decimals": 0,
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 1,
        "fillGradient": 0,
        "gridPos": {
          "h": 8,
          "w": 24,
          "x": 0,
          "y": 145
        },
        "hiddenSeries": false,
        "id": 603,
        "legend": {
          "avg": false,
          "current": false,
          "max": false,
          "min": false,
          "show": false,
          "total": false,
          "values": false
        },
        "lines": false,
        "linewidth": 1,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 2,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": false,
            "expr": "sort(sum(kafka_server_replica_manager_partitioncount{env=\"cluster-demo\", instance=\"jmx-kafka101:5556\", job=\"kafka\", service=\"kafka-broker\"}) by (instance))",
            "format": "time_series",
            "instant": true,
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "Instance Broker: {{instance}}",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "Count Partition per Broker",
        "tooltip": {
          "shared": false,
          "sort": 2,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "series",
          "show": true,
          "values": [
            "current"
          ]
        },
        "yaxes": [
          {
            "decimals": 0,
            "format": "none",
            "logBase": 2,
            "show": true
          },
          {
            "decimals": 0,
            "format": "none",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": true,
          "alignLevel": 0
        }
      },
      {
        "collapsed": false,
        "datasource": {
          "type": "prometheus",
          "uid": "OYKLxrO4k"
        },
        "gridPos": {
          "h": 1,
          "w": 24,
          "x": 0,
          "y": 153
        },
        "id": 159,
        "panels": [],
        "title": "JVM",
        "type": "row"
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 1,
        "fillGradient": 0,
        "gridPos": {
          "h": 9,
          "w": 12,
          "x": 0,
          "y": 154
        },
        "hiddenSeries": false,
        "id": 161,
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "max": true,
          "min": true,
          "show": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 1,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 2,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "kafka_jvm_thread_count{env=\"cluster-demo\", instance=\"jmx-kafka101:5556\", job=\"kafka\", service=\"kafka-broker\"}",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "{{instance}}",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "JVM Threads Current",
        "tooltip": {
          "shared": true,
          "sort": 0,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "format": "none",
            "logBase": 1,
            "show": true
          },
          {
            "format": "short",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 1,
        "fillGradient": 0,
        "gridPos": {
          "h": 9,
          "w": 12,
          "x": 12,
          "y": 154
        },
        "hiddenSeries": false,
        "id": 163,
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "max": true,
          "min": true,
          "show": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 1,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 5,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "sum without(area)(kafka_jvm_os_committedvirtualmemorysize{env=\"cluster-demo\", instance=\"jmx-kafka101:5556\", job=\"kafka\", service=\"kafka-broker\"})\n#sum without(area)(jvm_memory_bytes_used{job=\"$job\",instance=~\"$broker\"} )",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "Broker - {{instance}}",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "JVM Memory Usage",
        "tooltip": {
          "shared": true,
          "sort": 0,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "format": "bytes",
            "logBase": 1,
            "show": true
          },
          {
            "format": "short",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 1,
        "fillGradient": 0,
        "gridPos": {
          "h": 9,
          "w": 12,
          "x": 0,
          "y": 163
        },
        "hiddenSeries": false,
        "id": 81,
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "max": true,
          "min": true,
          "show": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 1,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 5,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "OYKLxrO4k"
            },
            "exemplar": true,
            "expr": "rate(kafka_jvm_os_processcputime{job=\"kafka\"}[1m])",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "Broker - {{instance}}",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "CPU Usage",
        "tooltip": {
          "shared": true,
          "sort": 0,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "format": "s",
            "label": "Usage/s",
            "logBase": 1,
            "show": true
          },
          {
            "format": "short",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      },
      {
        "aliasColors": {},
        "bars": false,
        "dashLength": 10,
        "dashes": false,
        "datasource": {
          "type": "prometheus",
          "uid": "OYKLxrO4k"
        },
        "description": "",
        "fieldConfig": {
          "defaults": {
            "links": []
          },
          "overrides": []
        },
        "fill": 1,
        "fillGradient": 0,
        "gridPos": {
          "h": 9,
          "w": 12,
          "x": 12,
          "y": 163
        },
        "hiddenSeries": false,
        "id": 83,
        "legend": {
          "alignAsTable": true,
          "avg": false,
          "current": true,
          "max": true,
          "min": true,
          "show": true,
          "total": false,
          "values": true
        },
        "lines": true,
        "linewidth": 1,
        "links": [],
        "nullPointMode": "null",
        "options": {
          "alertThreshold": true
        },
        "paceLength": 10,
        "percentage": false,
        "pluginVersion": "8.4.5",
        "pointradius": 5,
        "points": false,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": false,
        "steppedLine": false,
        "targets": [
          {
            "expr": "sum without(gc)(rate(jvm_gc_collection_seconds_sum{job=\"$job\",instance=~\"$broker\"}[1m]))",
            "format": "time_series",
            "interval": "",
            "intervalFactor": 1,
            "legendFormat": "{{instance}}",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeRegions": [],
        "title": "Time spent in GC",
        "tooltip": {
          "shared": true,
          "sort": 0,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "mode": "time",
          "show": true,
          "values": []
        },
        "yaxes": [
          {
            "format": "ms",
            "logBase": 1,
            "show": true
          },
          {
            "format": "short",
            "logBase": 1,
            "show": true
          }
        ],
        "yaxis": {
          "align": false
        }
      }
    ],
    "refresh": "1m",
    "schemaVersion": 35,
    "style": "dark",
    "tags": [
      "stable",
      "kafka"
    ],
    "templating": {
      "list": [
        {
          "current": {
            "isNone": true,
            "selected": false,
            "text": "None",
            "value": ""
          },
          "datasource": {
            "type": "prometheus",
            "uid": "OYKLxrO4k"
          },
          "definition": "label_values(kafka_controller_kafkacontroller_controllerstate, job)",
          "hide": 0,
          "includeAll": false,
          "label": "job",
          "multi": false,
          "name": "job",
          "options": [],
          "query": {
            "query": "label_values(kafka_controller_kafkacontroller_controllerstate, job)",
            "refId": "Prometheus-job-Variable-Query"
          },
          "refresh": 1,
          "regex": "",
          "skipUrlSync": false,
          "sort": 0,
          "tagValuesQuery": "",
          "tagsQuery": "",
          "type": "query",
          "useTags": false
        },
        {
          "current": {
            "selected": false,
            "text": "All",
            "value": "$__all"
          },
          "datasource": {
            "type": "prometheus",
            "uid": "OYKLxrO4k"
          },
          "definition": "label_values(kafka_controller_kafkacontroller_controllerstate{job=\"$job\"}, instance)",
          "hide": 0,
          "includeAll": true,
          "label": "Broker",
          "multi": true,
          "name": "broker",
          "options": [],
          "query": {
            "query": "label_values(kafka_controller_kafkacontroller_controllerstate{job=\"$job\"}, instance)",
            "refId": "Prometheus-broker-Variable-Query"
          },
          "refresh": 1,
          "regex": "",
          "skipUrlSync": false,
          "sort": 0,
          "tagValuesQuery": "",
          "tagsQuery": "",
          "type": "query",
          "useTags": false
        },
        {
          "current": {
            "selected": false,
            "text": "All",
            "value": "$__all"
          },
          "datasource": {
            "type": "prometheus",
            "uid": "OYKLxrO4k"
          },
          "definition": "label_values(kafka_cluster_partition_replicascount{job=\"$job\"}, topic)",
          "hide": 0,
          "includeAll": true,
          "label": "Topic",
          "multi": true,
          "name": "topic",
          "options": [],
          "query": {
            "query": "label_values(kafka_cluster_partition_replicascount{job=\"$job\"}, topic)",
            "refId": "Prometheus-topic-Variable-Query"
          },
          "refresh": 2,
          "regex": "",
          "skipUrlSync": false,
          "sort": 0,
          "tagValuesQuery": "",
          "tagsQuery": "",
          "type": "query",
          "useTags": false
        },
        {
          "current": {
            "isNone": true,
            "selected": false,
            "text": "None",
            "value": ""
          },
          "datasource": {
            "type": "prometheus",
            "uid": "OYKLxrO4k"
          },
          "definition": "query_result(count(up{job=~\"$job\"}))",
          "hide": 2,
          "includeAll": false,
          "label": "",
          "multi": false,
          "name": "online_broker",
          "options": [],
          "query": {
            "query": "query_result(count(up{job=~\"$job\"}))",
            "refId": "Prometheus-online_broker-Variable-Query"
          },
          "refresh": 1,
          "regex": "/.* ([^\\ ]*) .*/",
          "skipUrlSync": false,
          "sort": 0,
          "tagValuesQuery": "",
          "tagsQuery": "",
          "type": "query",
          "useTags": false
        }
      ]
    },
    "time": {
      "from": "now-1h",
      "to": "now"
    },
    "timepicker": {
      "hidden": false,
      "refresh_intervals": [
        "5s",
        "10s",
        "30s",
        "1m",
        "5m",
        "15m",
        "30m",
        "1h",
        "2h",
        "1d"
      ],
      "time_options": [
        "5m",
        "15m",
        "1h",
        "6h",
        "12h",
        "24h",
        "2d",
        "7d",
        "30d"
      ]
    },
    "timezone": "",
    "title": "Kafka Metrics_VF",
    "uid": "5nhADrDWk",
    "version": 9,
    "weekStart": ""
  }