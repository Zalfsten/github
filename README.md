# Semantic Versioning mit GitHub Actions und GitVersion

Dieses Repository implementiert einen automatischen Semantic Versioning Workflow mit GitHub Actions und GitVersion.

## Workflow

### Branch-Strategie

- **main**: Hauptbranch, protected, keine direkten Commits erlaubt
- **feature/\***: Feature-Branches für Entwicklung

### Pull Request Workflow

1. Erstelle einen Feature-Branch: `git checkout -b feature/mein-feature`
2. Entwickle dein Feature und pushe es
3. Erstelle einen Pull Request nach `main`
4. **Wichtig**: Füge eines der folgenden Labels zum PR hinzu:
   - `major version`: für breaking changes (1.0.0 → 2.0.0)
   - `minor version`: für neue Features (1.0.0 → 1.1.0)
   - `patch version`: für Bugfixes (1.0.0 → 1.0.1)

### Automatische Versionierung

Beim Mergen eines Pull Requests:

1. Der `enforce-pr-labels` Workflow überprüft, dass genau ein Versions-Label gesetzt ist
2. Der `version-bump` Workflow:
   - Verwendet GitVersion um die neue Version basierend auf dem Label zu berechnen
   - Erstellt einen Git-Tag mit der neuen Version
   - Erstellt ein GitHub Release

### Manuelle Versionierung

Für manuelle Releases kann der `version-bump` Workflow auch manuell ausgelöst werden:

1. Gehe zu Actions → Version Bump and Release
2. Klicke auf "Run workflow"
3. Wähle den Versions-Typ (major/minor/patch)

## Workflows

### 1. Enforce PR Labels

- **File:** `.github/workflows/enforce-pr-labels.yml`
- **Purpose:** Stellt sicher, dass alle Pull Requests zum main Branch die erforderlichen Labels haben: 'major version', 'minor version', oder 'patch version'. Ohne eines dieser Labels kann der PR nicht gemergt werden.

### 2. Version Bump and Release

- **File:** `.github/workflows/version-bump.yml`
- **Purpose:** Nutzt GitVersion um automatisch die Versionsnummer basierend auf den PR-Labels zu erhöhen. Erstellt Git-Tags und GitHub Releases.

## Labels

Die folgenden Labels müssen in deinem Repository erstellt werden:

- `major version` (rot/red)
- `minor version` (blau/blue)
- `patch version` (grün/green)

## Setup

1. Stelle sicher, dass der `main` Branch protected ist
2. Erstelle die erforderlichen Labels in deinem Repository
3. Die Workflows werden automatisch ausgeführt

## GitVersion Konfiguration

Die GitVersion Konfiguration wird dynamisch basierend auf den PR-Labels erstellt. Die Base-Konfiguration findest du in `GitVersion.yml`.

## Beispiel

```bash
# Feature entwickeln
git checkout -b feature/neue-api
# ... Änderungen machen ...
git push origin feature/neue-api

# PR erstellen und Label "minor version" hinzufügen
# Nach dem Merge wird automatisch von 1.0.0 auf 1.1.0 erhöht
```
